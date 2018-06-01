# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from stone.items import StoneItem


class Stone365Spider(scrapy.Spider):
    name = 'stone365'
    base_url = 'http://company.stone365.com'
    allowed_domains = ['stone365.com']
    start_urls = ['http://company.stone365.com/list-ar17.html']

    def parse(self, response):
        list = response.xpath('//a[@class="pricemsg"]/@href').extract()
        next_page = response.xpath('//div[@class="fenpage qyhylist"]//a[text()="下一页"]/@href').extract()
        if next_page:
            yield Request(url=self.base_url + next_page[0], callback=self.parse)
        for i in list:
            yield Request(url=i, callback=self.parse_item)

    def parse_item(self, response):
        item = StoneItem()
        item['company'] = response.xpath('//*[@class="contact_info"]/li[1]/text()').extract()[0]
        item['name'] = response.xpath('//*[@class="contact_info"]/li[2]/text()').extract()[0]
        item['tel'] = self.get_first_item(response.xpath('//*[@class="contact_info"]/li[3]/text()').extract())
        item['ph'] = self.get_first_item(response.xpath('//*[@class="contact_info"]/li[4]/text()').extract()[0])
        item['fax'] = self.get_first_itm(response.xpath('//*[@class="contact_info"]/li[5]/text()').extract()[0])
        item['email'] = self.get_first_item(response.xpath('//*[@class="contact_info"]/li[6]/text()').extract()[0])
        item['https'] = self.get_first_item(response.xpath('//*[@class="contact_info"]/li[7]/text()').extract()[0])
        item['address'] = self.get_first_item(response.xpath('//*[@class="contact_info"]/li[8]/text()').extract()[0])
        yield item

    @staticmethod
    def get_first_item(self, list):
        if list:
            return list[0]
        return ''
