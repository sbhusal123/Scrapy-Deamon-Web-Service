# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from scrapy_splash import SplashRequest

class SmartPhonesSpider(scrapy.Spider):
    name = 'smart_phones'
    allowed_domains = ['www.daraz.com.np']

    script = '''
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(1))
            return splash:html()
        end
    '''

    def start_requests(self):
        yield SplashRequest(url="https://www.daraz.com.np/smartphones/",\
            callback=self.parse, endpoint="execute", args={'lua_source': self.script})

    def parse(self, response):
        # inspect_response(response, self)
        products = response.xpath('//div[@class="c3KeDq"]')
        for product in products:
            yield {
                'title': product.xpath('.//div[2]/a/text()').get(),
                'discounted_price': product.xpath('.//div[3]/span/text()').get(),
            }

        next_disabled = response.xpath('//ul[@class="ant-pagination "]/li[@title="Next Page"]/@aria-disabled').get()

        if next_disabled != "true":
            next_page = response.xpath('//ul[@class="ant-pagination "]/li[contains(@class,"ant-pagination-item-active")]/following::li/a/@href').get()
            next_url = response.urljoin(next_page)
            yield SplashRequest(url=next_url,callback=self.parse, \
                endpoint="execute", args={'lua_source': self.script})