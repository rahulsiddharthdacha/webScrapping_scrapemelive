# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Webcrawl2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    price=scrapy.Field()
    desc=scrapy.Field()
    stock=scrapy.Field()
    categories=scrapy.Field()
    SKU=scrapy.Field()
    tags=scrapy.Field()
    breadcrumbs=scrapy.Field()
    product_url=scrapy.Field()
