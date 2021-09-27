# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AvantaItem(scrapy.Item):
   
    url = scrapy.Field()
    title = scrapy.Field()
    image = scrapy.Field()
    video = scrapy.Field()
    category = scrapy.Field()
    stats = scrapy.Field()
    ingredients = scrapy.Field()
    method = scrapy.Field()
    about = scrapy.Field()
   
