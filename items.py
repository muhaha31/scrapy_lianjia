# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CqFangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    place = scrapy.Field()
    model = scrapy.Field()
    area = scrapy.Field() #面积
    average_price = scrapy.Field()
    link = scrapy.Field()
    lonlat = scrapy.Field()
    city = scrapy.Field()
    assesses = scrapy.Field()

class LonLatItem(scrapy.Item):
    longitude = scrapy.Field()
    latitude = scrapy.Field()



class AssessItem(scrapy.Item):
    all_grade = scrapy.Field()
    ambitus = scrapy.Field()
    traffic = scrapy.Field()
    green = scrapy.Field()


