# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    product_title=scrapy.Field()
    product_price_whole=scrapy.Field()
    product_price_fraction=scrapy.Field()
    product_image_url=scrapy.Field()
    product_details_tags=scrapy.Field()
    product_details_tags_values=scrapy.Field()

    
    pass
