# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['r18.com']
    start_urls = [
        'https://www.r18.com/videos/vod/movies/detail/-/id=cjod00196/'
    ]

    def parse(self, response):
        url = 'https://www.r18.com/videos/vod/movies/detail/-/id=cjod00196/'
        item = {
            'cover_img' : response.xpath("//img[@itemprop='image']/@src").get()
        }
        yield scrapy.Request(
            url,
            callback = self.parse_test,
            meta=dict(item=item)
        )
        yield scrapy.Request(url, callback=self.parse) 

    def parse_test(self, response):
        item = response.meta["item"]
        yield item