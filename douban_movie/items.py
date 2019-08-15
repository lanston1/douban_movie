# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field



class DoubanMovieItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type_name = Field()
    titie = Field()
    rank = Field()
    url = Field()
    actors = Field()
    cover_url = Field()
    regions = Field()
    release_date = Field()
    score = Field()
    types = Field()
    vote_count = Field()

