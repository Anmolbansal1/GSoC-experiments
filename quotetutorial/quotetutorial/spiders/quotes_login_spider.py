import scrapy
from ..items import QuotetutorialItem
from scrapy.http import FormRequest

class QuoteLoginSpider(scrapy.Spider):
    name = "quotes_login"
    start_urls = [
        "http://quotes.toscrape.com/login"
    ]
    page_number = 2

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'attreya01@gmail.com',
            'password': 'dsadsdsa'
        }, callback=self.start_scraping)
    
    def start_scraping(self, response):
        item = QuotetutorialItem

        all_div_quotes = response.css('div.quote')
        
        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tags = quote.css('.tag::text').extract()
            
            item['title'] = title
            item['author'] = author
            item['tags'] = tags

            yield item

        next_page = 'http://quotes.toscrape.com/page/'+ str(QuoteLoginSpider.page_number) + '/'

        if QuoteLoginSpider.page_number < 11:
            QuoteLoginSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
