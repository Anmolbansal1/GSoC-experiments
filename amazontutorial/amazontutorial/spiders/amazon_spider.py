# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.in/s?bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&fst=as%3Aoff&qid=1558937304&rnid=2684818031&ref=lp_976389031_nr_p_n_publication_date_0'
    ]

    def parse(self, response):
        item = AmazontutorialItem()

        name = response.css('.a-color-base.a-text-normal::text').extract()
        author = response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        price = response.css('.a-spacing-top-small .a-price:nth-child(1) .a-price-whole').css('::text').extract()
        imageLink = response.css('.s-image::attr(src)').extract()

        item['name'] = name
        item['author'] = author
        item['price'] = price
        item['imageLink'] = imageLink
        yield item
