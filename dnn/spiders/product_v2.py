# -*- coding: utf-8 -*-
import scrapy
import re
from dnn.user_config import product_v2


class ProductSpider(scrapy.Spider):
    name, allowed_domains, start_urls = product_v2
    
    def parse(self, response):
        actress_urls = response.xpath("//ul[contains(@class, 'nml07')]/li/a/@href").getall()
        for url in actress_urls:
            page_url = url.replace("pagesize=30", "pagesize=120")
            yield scrapy.Request(
                page_url,
                callback=self.parse_product
            )
        next_page = response.xpath("//li[@class='next']/a/@href").get()
        print("开始下一页的爬取")
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_product(self, response):
        product_list = response.xpath("//ul[contains(@class, 'type01')]/li")
        for product in product_list:
            item = dict()
            item["title"] = product.xpath(".//dt/text()").get()
            price = product.xpath(".//dd/text()").get()
            item["price"] = "$" + self.clean(price, r"\d+\.\d+")
            product_url = product.xpath("./a/@href").get()
            item["product_url"] = product_url.split("?")[0] if product_url is not None else None
            cover = product.xpath(".//img/@data-original").get()
            item["cover_image"] = cover.replace("ps.jpg", "pl.jpg")
            yield scrapy.Request(
                item["product_url"] + '?lg=zh',
                callback=self.parse_detail,
                meta=dict(item=item)
            )
        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_product)
    
    def parse_detail(self, response):
        item = response.meta["item"]
        date = response.xpath("//dd[@itemprop='dateCreated']/text()").get()
        item["pub_date"] = self.clean(date)
        duration = response.xpath("//dd[@itemprop='duration']/text()").get()
        item["duration"] = self.clean(duration)
        director = response.xpath("//dd[@itemprop='director']/text()").get()
        item["director"] = self.clean(director)

        deatil = response.xpath("//div[@class='product-details']")
        content_id= deatil.xpath("./dl[2]/dd[2]/text()").get()
        item["content_id"] = self.clean(content_id)
        dvd_id = deatil.xpath("./dl[2]/dd[3]/text()").get()
        item["dvd_id"] = self.clean(dvd_id)

        series = deatil.xpath("./dl[2]/dd[4]/a")
        item["series"] = self.parse_id_name(series)
        
        company = deatil.xpath(".//dd[@itemprop='productionCompany']/a")
        item["company"] = self.parse_id_name(company)
        
        actress = deatil.xpath(".//div[@itemprop='actors']//a")
        item["actress"] = self.parse_id_name(actress, "./span/text()")

        genre = deatil.xpath(".//a[@itemprop='genre']")
        item["genre"] = self.parse_id_name(genre)
        
        item["sample_images "] = response.xpath("//ul[contains(@class, 'preview-grid')]//img/@data-original").getall()
        item["sample_movie"] = response.xpath("//a[@class='js-view-sample']/@data-video-high").get()

        yield item

    def parse_id(self, s):
        """从url中解析id"""
        ret = re.findall(r'id=\d+', s)
        return ret[0].split("=")[1] if len(ret) > 0 else None
    
    def clean(self, s, rule = r"\S+"):
        ret = re.findall(rule, s)
        return ret[0] if (s is not None) & (len(ret) >0) else None

    def parse_id_name(self, s, path="./text()"):
        id = s.xpath("./@href").getall()
        name = s.xpath(path).getall()
        return [{"id": self.parse_id(id[i]), "name": self.clean(name[i])} for i in range(len(id))] if (len(id) > 0) & (len(name) > 0)  else None
        


