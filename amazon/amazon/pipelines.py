# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class AmazonPipeline:
    def __init__(self) :
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn=sqlite3.connect("amazonscrape.db")
        self.curr=self.conn.cursor()
    
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS amazonscrape_tb""")
        self.curr.execute("""create table amazonscrape_tb(

            product_title text,
            product_price_whole text,
            product_price_fraction text,
            product_image_url text,
            product_details_tags blob,
            product_details_tags_values blob

        )""")
    
    def process_item(self, item, spider):

        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute("""insert into amazonscrape_tb values(?,?,?,?,?,?)""",(
            
            item['product_title'],
            item['product_price_whole'],
            item['product_price_fraction'],
            item['product_image_url'],
            item['product_details_tags'],
            item['product_details_tags_values']
        ))
        self.conn.commit()