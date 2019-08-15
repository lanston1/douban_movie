# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from urllib.parse import urlencode, unquote
import json
from douban_movie.items import DoubanMovieItem
from scrapy.utils.project import get_project_settings
import re

class DoubanSpider(Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']

    def __init__(self, movie_category=None):
        self.mySetting = get_project_settings()
        self.movie_category = self.mySetting['MOVIE_CATEGORY']
        super(DoubanSpider, self).__init__()


    def start_requests(self):
        for v in self.movie_category.values():
            for i in range(10):
                percentage = 100
                params = {
                    'type':v,
                    'interval_id':"{}:{}".format(percentage-i*10, percentage-i*10-10)
                }
                base_url = 'https://movie.douban.com/j/chart/top_list_count?'
                url = base_url + urlencode(params)
                yield Request(url=url, meta={'dont_redirect': True,'download_timeout':10}, callback=self.parse_count)

    def parse_count(self, response):
        data = json.loads(response.text)
        count = int(data.get('total'))
        movie_type = re.search('type=(.*?)&', unquote(response.url)).group(1)
        interval_id = re.search('interval_id=(.*)', unquote(response.url)).group(1)
        params = {
            'type':movie_type,
            'interval_id': interval_id,
            'start': 0,
            'limit':count
        }
        base_url = 'https://movie.douban.com/j/chart/top_list?'
        url = base_url + urlencode(params)
        yield Request(url=url, meta={'dont_redirect': True,'download_timeout':10}, callback=self.parse_detail)



    def parse_detail(self, response):
        type_name = None
        for k,v in self.movie_category.items():
            if str(v) == re.search('type=(.*?)&', unquote(response.url)).group(1):
                type_name = k
        datas = json.loads((response.text))
        for data in datas:
            type_name = type_name
            titie = data.get('title')
            rank = data.get('rank')
            url = data.get('url')
            actors = data.get('actors')
            cover_url = data.get('cover_url')
            regions = data.get('regions')
            release_date = data.get('release_date')
            score = data.get('score')
            types = data.get('types')
            vote_count = data.get('vote_count')
            douban_item = DoubanMovieItem()
            for field in douban_item.fields:
                try:
                    douban_item[field] = eval(field)
                except:
                    print('Field is Not Defined', field)
            yield douban_item


