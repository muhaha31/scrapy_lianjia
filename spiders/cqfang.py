# _*_ coding: utf-8 -*-
import scrapy
import requests
import re
import time
import traceback
import random
from lxml import etree
from ..items import CqFangItem, LonLatItem, AssessItem
from scrapy_redis.spiders import RedisSpider
from lxml.html import HtmlElement, tostring

class CqFangSpider(RedisSpider):
    name = 'cqspider'
    redis_key = 'chongqingspider:urls'
    start_urls = 'http://cq.fang.lianjia.com/loupan/'

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls, method='GET', dont_filter = True, callback=self.parse)

    def parse(self, response):
        lists = response.body.decode('utf-8')
        selector = etree.HTML(lists)
        area_list = selector.xpath('//*[@id="filter-options"]/dl[1]/dd/div/a')[1:10]
        for area in area_list:
            try:
                area_han = area.xpath('text()').pop() #区
                area_pin = area.xpath('@href').pop().split('/')[2]
                area_url = 'http://cq.fang.lianjia.com/loupan/{}'.format(area_pin)
                print(area_url)
                yield scrapy.Request(url=area_url, callback=self.detail_url, dont_filter = True, meta={"id1":area_han, "id2": area_pin} )
            except Exception:
                pass

    
    def get_lonlat(self, url):
        try:
            apiUrl = "http://api.ip.data5u.com/dynamic/get.html?order=08903ff28b3c5147a042d2585211e257";
            res = requests.get(apiUrl).text
            proxies = {}
            ips = res.split("\n");
            proxies['http'] = ips[0]
            url = 'http://cq.fang.lianjia.com'+url
            p = requests.get(url, proxies=proxies)
            contents = etree.HTML(p.content.decode('utf-8'))
            latitude = contents.xpath('/html/body/div[2]/script[7]/text()').pop()
            regex = '''parseFloat.+?\)'''
            items = re.findall(regex, latitude)
            lon = items[0][12:-2]
            lat = items[1][12:-2]
            lonlat = LonLatItem()
            lonlat['longitude'] = lon
            lonlat['latitude'] = lat
            print('经纬度：',lonlat['longitude'],lonlat['latitude'])
        except Exception:
            traceback.print_exc()
        return lonlat

    def get_assess(self, url):
        try:
            apiUrl = "http://api.ip.data5u.com/dynamic/get.html?order=08903ff28b3c5147a042d2585211e257";
            res = requests.get(apiUrl).text
            proxies = {}
            ips = res.split("\n");
            proxies['http'] = ips[0]
            url = 'http://cq.fang.lianjia.com'+url
            p = requests.get(url, proxies=proxies)
            contents = etree.HTML(p.content.decode('utf-8'))
            all_grade = contents.xpath('//*[@id="user-comment"]/div[1]/div[1]/div[1]/span[1]/text()').pop()
            ambitus = contents.xpath('//*[@id="user-comment"]/div[1]/div[1]/div[2]/div[1]/i/text()').pop()
            traffic = contents.xpath('//*[@id="user-comment"]/div[1]/div[1]/div[2]/div[2]/i/text()').pop()
            green = contents.xpath('//*[@id="user-comment"]/div[1]/div[1]/div[2]/div[3]/i/text()').pop()
            access = AssessItem()
            access['all_grade'] = all_grade
            access['ambitus'] = ambitus
            access['traffic'] = traffic
            access['green'] = green
            print('评分',all_grade,'-',ambitus,'-',traffic,'-',green)
        except Exception:
            traceback.print_exc()
        return access

    def detail_url(self, response):
        'http://cq.fang.lianjia.com/loupan/jiangbei/pg1/'
        print(response.meta)
        for i in range(1, 9):
            print('start detail')
            url = 'http://cq.fang.lianjia.com/loupan/{}/pg{}'.format(response.meta['id2'],str(i))
            time.sleep(1)
            yield scrapy.Request(url=url, callback=self.detail_parse, dont_filter = True, meta = response.meta)
    

    def detail_parse(self, response):
        print(response.meta)
        try:
            contents = etree.HTML(response.body.decode(response.encoding))
            houselist = contents.xpath('//*[@id="house-lst"]/li')
            time.sleep(2)
            for house in houselist:
                try:
                    item = CqFangItem()
                    item['title'] = house.xpath('div[2]/div[1]/h2/a/text()').pop()
                    print(item['title'])
                    item['place'] = house.xpath('div[2]/div[1]/div[1]/span/text()').pop()
                    item['average_price'] = house.xpath('div[2]/div[2]/div/div/span/text()').pop()
                    print(item['average_price'])
                    item['model'] = house.xpath('div[2]/div/div[2]/text()').pop()
                    print(item['model'])
                    item['area'] = house.xpath('div[2]/div/div[2]/span/text()').pop()
                    print(item['area'])
                    item['link'] = house.xpath('div[2]/div[1]/h2/a/@href').pop()
                    print(item['link'])
                    item['city'] = response.meta["id1"]
                    print(item['city'])
                    self.url_detail = house.xpath('div[2]/div[1]/h2/a/@href').pop()
                    item['lonlat'] = self.get_lonlat(self.url_detail)
                    item['assesses'] = self.get_assess(self.url_detail)
                except Exception:
                    traceback.print_exc()
                yield item
        except Exception:
            traceback.print_exc()

