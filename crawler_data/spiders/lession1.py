# -*- coding: utf-8 -*-
import scrapy


class Lession1Spider(scrapy.Spider):
    name = 'lession1'
    allowed_domains = ['vnexpress.net']
    start_urls = ['https://vnexpress.net/loi-thu-toi-muon-mang-cua-ke-giet-nguoi-hang-loat-4104544.html']

    def parse(self, response):
        self.logger.info('start crawl')
        self.logger.info('doing crawl...')
        text = response.xpath("//p").extract()
        print(text)
        self.logger.info('end crawl')

