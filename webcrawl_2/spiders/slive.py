import scrapy
from ..items import Webcrawl2Item

class SliveSpider(scrapy.Spider):
    name = 'slive'
    # allowed_domains = ['scrapeme.live/shop/']
    # start_urls = ['http://scrapeme.live/shop//']
    def start_requests(self):
        url='https://scrapeme.live/shop/page/{}/'
        for i in range(1,11):
            yield scrapy.Request(url.format(i),callback=self.parse_d)
    def parse_d(self,response):
        urls= response.xpath('//ul[@class="products columns-4"]//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]/@href').extract()
        for url in urls:
            yield scrapy.Request(url,callback=self.parse)
    def parse(self, response):
        items=Webcrawl2Item()
        items['name']="".join(response.xpath('//h1[@class="product_title entry-title"]/text()').extract())
        items['price']="".join(response.xpath('//div[@class="summary entry-summary"]/p[@class="price"]/span[@class="woocommerce-Price-amount amount"]/text()').extract())
        items['desc']="".join(response.xpath('//div[@class="summary entry-summary"]/div[@class="woocommerce-product-details__short-description"]/p/text()').extract())
        items['stock']= response.xpath('//div[@class="summary entry-summary"]/p[@class="stock in-stock"]/text()').extract()[0].split()[0]
        items['categories']=",".join(response.xpath('//div[@class="summary entry-summary"]/div[@class="product_meta"]/span[@class="posted_in"]/a[@rel="tag"]/text()').extract())
        items['SKU']="".join(response.xpath('//div[@class="summary entry-summary"]/div[@class="product_meta"]/span[@class="sku_wrapper"]/span/text()').extract())
        items['tags']=",".join(response.xpath('//div[@class="summary entry-summary"]/div[@class="product_meta"]/span[@class="tagged_as"]/a[@rel="tag"]/text()').extract())
        items['product_url']=response.url
        items['breadcrumbs']="|".join(response.xpath('//nav[@class="woocommerce-breadcrumb"]/child::a/text()').extract()+response.xpath('//nav[@class="woocommerce-breadcrumb"]/text()').extract())
        yield items
    
        
