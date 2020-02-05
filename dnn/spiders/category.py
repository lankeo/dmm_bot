# -*- coding: utf-8 -*-
import scrapy
import re
from dnn.user_config import category


class CategorySpider(scrapy.Spider):
    name, allowed_domains, start_urls = category
    
    def parse(self, response):
        cate_bg = response.xpath("//div[@class='breadcrumbs']//li[4]/a/text()").get()
        cate_title = response.xpath("//div[@class='col01']/h1/text()").getall()
        cates = response.xpath("//div[@id='contents']/ul")
        for cate in cates:
            genre = cate.xpath("./li")
            for i in genre:
                item = dict()
                item["cate_l"] = cate_bg.replace("動畫", "动画")
                item["cate_m"] = cate_title[cates.index(cate)]
                item["genre_id"] = self.parse_id(i.xpath("./a/@href").get())
                name = i.xpath(".//p[2]/text()").get()
                item["name"] = name if name is not None else i.xpath("./a/text()").get()
                item["image_url"] = i.xpath(".//img/@data-original").get()
                yield item

    def parse_id(self, s):
        """从url中解析id"""
        ret = re.findall(r'id=\d+', s)
        return ret[0].split("=")[1] if len(ret) > 0 else None
            
            


