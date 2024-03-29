# -*- coding: utf-8 -*-

# Scrapy settings for douban_movie project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'douban_movie'

SPIDER_MODULES = ['douban_movie.spiders']
NEWSPIDER_MODULE = 'douban_movie.spiders'

MONGO_URI = 'localhost'
MONGO_DATABASE = 'douban_movie'
MONGO_PASSWORD = None


MOVIE_CATEGORY = {'剧情':11, '喜剧':24, '动作':5, '爱情':13, '科幻':17, '动画':25, '悬疑':10, '惊悚':19, '恐怖':20, '纪录片':1, '短片':23, '情色':6, '同性':26, '音乐':14, '歌舞':7, '家庭':28, '儿童':8, '传记':2, '历史':4, '战争':22, '犯罪':3, '西部':27, '奇幻':16, '冒险':15, '灾难':12, '武侠':29, '古装':30, '运动':18, '黑色电影':31}

#阿布云设置
PROPXYHOST = 'http-dyn.abuyun.com'
PROPXYPORT = '9020'
PROPXYUSER = 'H01234567890123D'
PROPXYPASS = '0123456789012345'




# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douban_movie (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'douban_movie.middlewares.DoubanMovieSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'douban_movie.middlewares.DoubanMovieDownloaderMiddleware': 543,
   'douban_movie.middlewares.RandomUserAgentMiddleware': 540,
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
   'douban_movie.middlewares.ProxyMiddleare': 530,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'douban_movie.pipelines.DoubanMoviePipeline': 300,
   'douban_movie.pipelines.MongoPipeline': 300,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
