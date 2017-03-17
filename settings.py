# -*- coding: utf-8 -*-

# Scrapy settings for cqfang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'cqfang'

SPIDER_MODULES = ['cqfang.spiders']
NEWSPIDER_MODULE = 'cqfang.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cqfang (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'cqfang.middlewares.CqfangSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'cqfang.middlewares.MyCustomDownloaderMiddleware': 543,
    'cqfang.middlewares.RandomUserAgent': 1, #随机user agent
    'cqfang.middlewares.ProxyMiddleware': 100, #代理需要用到
    # 'scrapy_crawlera.CrawleraMiddleware': 600, #crawlera代理用到
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'cqfang.pipelines.CqfangPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

SCHEDULER = "scrapy_redis.scheduler.Scheduler"    #调度
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  #去重
SCHEDULER_PERSIST = True     #不清理Redis队列
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"    #队列

ITEM_PIPELINES = {
   'cqfang.pipelines.CqfangPipeline': 300,
}

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = "chongqing"
MONGODB_DOCNAME = "house"


USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

PROXIES = [
    {'ip_port': '116.53.164.34:8998','user_pass':''},
    {'ip_port': '49.84.92.136:8998','user_pass':''},
    {'ip_port': '183.59.159.180:8081','user_pass':''},
    {'ip_port': '115.220.145.92:808','user_pass':''},
    {'ip_port': '121.204.165.177:8118','user_pass':''},
    {'ip_port': '175.155.24.39:808','user_pass':''},
    {'ip_port': '182.87.68.50:8998','user_pass':''},
    {'ip_port': '113.99.216.190:8081','user_pass':''},
    {'ip_port': '115.230.15.82:808','user_pass':''},
    {'ip_port': '106.5.51.148:8998','user_pass':''},
    {'ip_port': '114.239.149.152:808','user_pass':''},
    {'ip_port': '113.12.141.227:8998','user_pass':''},
    {'ip_port': '182.91.57.198:8081','user_pass':''},
    {'ip_port': '114.239.127.170:808','user_pass':''},
    {'ip_port': '119.5.0.34:808','user_pass':''},
    {'ip_port': '117.83.55.178:8998','user_pass':''},
    {'ip_port': '106.46.136.113:808','user_pass':''},
    {'ip_port': '222.169.193.162:8099','user_pass':''},
    {'ip_port': '222.169.138.134:8998','user_pass':''},
    {'ip_port': '124.88.67.39:83','user_pass':''},
    {'ip_port': '61.150.88.84:8998','user_pass':''},
    {'ip_port': '111.174.223.230:8081','user_pass':''},
    {'ip_port': '180.136.190.111:8998','user_pass':''},
    {'ip_port': '119.5.0.41:808','user_pass':''},
    {'ip_port': '119.5.0.62:808','user_pass':''},
    {'ip_port': '183.33.216.208:8998','user_pass':''},
    {'ip_port': '175.155.25.28:808','user_pass':''},
    {'ip_port': '111.76.137.4:808','user_pass':''},
    {'ip_port': '113.74.115.182:9797','user_pass':''},
    {'ip_port': '114.239.144.196:808','user_pass':''},
    {'ip_port': '124.88.67.54:82','user_pass':''},
    {'ip_port': '218.77.97.112:3128','user_pass':''},
    {'ip_port': '123.11.9.127:9999','user_pass':''},
    {'ip_port': '114.239.147.187:808','user_pass':''},
    {'ip_port': '183.128.179.41:808','user_pass':''},
    {'ip_port': '117.71.104.83:8998','user_pass':''},
    {'ip_port': '111.72.127.5:808','user_pass':''},
    {'ip_port': '221.199.71.82:8888','user_pass':''},
    {'ip_port': '163.125.157.26:6666','user_pass':''},
    {'ip_port': '182.91.59.204:8081','user_pass':''},
    {'ip_port': '119.5.0.60:808','user_pass':''},
    {'ip_port': '115.220.5.77:808','user_pass':''},
    {'ip_port': '183.2.219.42:3129','user_pass':''},
    {'ip_port': '114.239.146.22:808','user_pass':''},
    {'ip_port': '221.3.6.2:8081','user_pass':''},
    {'ip_port': '115.220.1.14:808','user_pass':''},
    {'ip_port': '111.72.127.33:808','user_pass':''},
    {'ip_port': '114.239.2.102:808','user_pass':''},
    {'ip_port': '106.46.136.14:808','user_pass':''},
    {'ip_port': '115.220.6.177:808','user_pass':''},
    {'ip_port': '49.64.16.38:8998','user_pass':''},
    {'ip_port': '114.239.144.144:808','user_pass':''},
    {'ip_port': '183.39.156.128:9797','user_pass':''},
    {'ip_port': '114.230.104.81:808','user_pass':''},
    {'ip_port': '115.220.146.203:808','user_pass':''},
    {'ip_port': '222.76.175.128:8088','user_pass':''},
    {'ip_port': '114.239.146.6:808','user_pass':''},
    {'ip_port': '106.46.136.178:808','user_pass':''},
    {'ip_port': '114.239.150.128:808','user_pass':''},
    {'ip_port': '111.76.197.206:8998','user_pass':''},
    {'ip_port': '101.230.214.25:8080','user_pass':''},
    {'ip_port': '119.5.1.43:808','user_pass':''},
    {'ip_port': '114.239.124.82:808','user_pass':''},
    {'ip_port': '116.53.166.76:8998','user_pass':''},
    {'ip_port': '175.155.24.27:808','user_pass':''},
    {'ip_port': '115.220.145.132:808','user_pass':''},
    {'ip_port': '106.46.136.194:808','user_pass':''},
    {'ip_port': '27.22.23.42:8998','user_pass':''},
    {'ip_port': '60.209.90.211:8888','user_pass':''},
    {'ip_port': '171.8.79.143:8080','user_pass':''},
    {'ip_port': '106.46.136.50:808','user_pass':''},
    {'ip_port': '122.228.140.214:8081','user_pass':''},
    {'ip_port': '115.220.0.37:808','user_pass':''},
    {'ip_port': '106.46.136.149:808','user_pass':''},
    {'ip_port': '27.18.197.7:8998','user_pass':''},
    {'ip_port': '110.152.1.72:8998','user_pass':''},
    {'ip_port': '106.46.136.193:808','user_pass':''},
    {'ip_port': '120.70.156.92:8998','user_pass':''},
    {'ip_port': '106.46.136.105:808','user_pass':''},
    {'ip_port': '124.88.67.52:843','user_pass':''},
    {'ip_port': '1.62.154.166:8081','user_pass':''},
    {'ip_port': '111.124.185.154:8998','user_pass':''},
    {'ip_port': '101.53.101.172:9999','user_pass':''},
    {'ip_port': '106.46.136.59:808','user_pass':''},
    {'ip_port': '113.123.79.51:808','user_pass':''},
    {'ip_port': '106.46.136.165:808','user_pass':''},
    {'ip_port': '175.155.25.10:808','user_pass':''},
    {'ip_port': '119.5.0.67:808','user_pass':''},
    {'ip_port': '60.160.34.4:3128','user_pass':''},
    {'ip_port': '114.239.0.208:808','user_pass':''},
    {'ip_port': '114.239.149.105:808','user_pass':''},
    {'ip_port': '122.228.140.213:8081','user_pass':''},
    {'ip_port': '27.18.117.206:8998','user_pass':''},
    {'ip_port': '106.46.136.51:808','user_pass':''},
    {'ip_port': '113.69.165.215:808','user_pass':''},
    {'ip_port': '119.5.220.27:808','user_pass':''},
    {'ip_port': '27.18.155.70:8998','user_pass':''},
    {'ip_port': '60.168.212.120:8998','user_pass':''},
    {'ip_port': '114.239.147.64:808','user_pass':''}
]

