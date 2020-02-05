# -*- coding: utf-8 -*-
import scrapy
from dnn.items import ActressItem
from dnn.user_config import actress


class R18Spider(scrapy.Spider):

    name, allowed_domains, start_urls = actress

    def parse(self, response):
        actress_list = response.xpath("//ul[contains(@class, 'nml07')]/li")
        for actress in actress_list:
            item = ActressItem()
            item["act_id"] = actress.xpath("./div[contains(@class, 'ico01')]/@data-follow-id").get()
            act_info = actress.xpath(".//img")
            item["avatar_url"] = act_info.xpath("./@src").get()
            item["name"] = act_info.xpath("./@alt").get()
            list_url = actress.xpath("./a/@href").get()
            item["list_url"] = list_url.replace("pagesize=30", "pagesize=120")
            item["_en"] = self.handle_name(item["avatar_url"])
            item["_zh"] = None
            yield item
        next_page = response.xpath("//li[@class='next']/a/@href").get()
        print("开始下一页的爬取")
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def handle_name(self, s):
        """ 处理ulr中的英文名"""
        return " ".join(s.split("/")[-1].split(".")[0].split("_")[::-1]).capitalize()

    