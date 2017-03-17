# Scrapy爬取链家数据



为防止被ban，在ProxyMiddleware中使用[http://data5u.com](http://data5u.com)的动态代理来获取代理IP。

```python
class ProxyMiddleware(object):
    def process_request(self, request, spider):
        order = ''
        apiUrl = "http://api.ip.data5u.com/dynamic/get.html?order=" + order;
        try:
            res = urllib.urlopen(apiUrl).read().strip("\n");
            ips = res.split("\n");
            proxy = random.choice(ips);
            request.meta['proxy'] = "http://%s" % proxy
            print "**************************"+ proxy +"**************************"
            time.sleep(2)
        except Exception as e:
            print(e)
```

##可视化

数据存入后，通过 `utils.py` 将数据从mongodb写入excel，上传到[http://bdp.cn](http://bdp.cn)来做可视化展示。