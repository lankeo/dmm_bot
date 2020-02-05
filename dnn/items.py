# -*- coding: utf-8 -*-
import scrapy


class ActressItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    act_id = scrapy.Field()
    name = scrapy.Field()
    _en = scrapy.Field()
    _zh = scrapy.Field()
    avatar_url = scrapy.Field()
    list_url = scrapy.Field()
    # _jp
    # cup
    # bust
    # waist
    # hip
    # height
    # birthday
    # blood_type
    # hobby
    # prefectures


# class ProductItem(scrapy.Item):
#     _id = scrapy.Field()
#     title = scrapy.Field()
#     price = scrapy.Field()
#     product_url = scrapy.Field()
#     cover_image = scrapy.Field()
#     pub_date = scrapy.Field()
#     duration = scrapy.Field()
#     director = scrapy.Field()
#     company = scrapy.Field()
#     content_id = scrapy.Field()
#     dvd_id = scrapy.Field()
#     sample_images = scrapy.Field()
#     sample_movie = scrapy.Field()
#     series = scrapy.Field()
#     genre = scrapy.Field()
#     actress = scrapy.Field()

# add "jp" to lager
# https://pics.dmm.co.jp/digital/video/miae00285/miae00285jp-6.jpg
# https://pics.dmm.co.jp/digital/video/miae00285/miae00285-6.jpg