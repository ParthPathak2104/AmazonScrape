


import scrapy
from urlgenerator import generateurls

urls=['https://www.amazon.de/dp/000417318X', 'https://www.amazon.fr/dp/000104348X']

class amazontestspider(scrapy.Spider):
    name="amazontest"
    start_urls = [
        urls[0]
    ]
    handle_httpstatus_list = [404]
    url_number=0

    def parse(self,response):
        product_price_whole=response.css("a.a-button-text span.a-color-base").css("::text").extract()
        product_price_whole_final=[]
        for product_price in product_price_whole:
            product_price=product_price.replace(u"\n",u"")
            product_price=product_price.replace(u" ",u"")
            product_price=product_price.replace(u"\xa0€",u"")
            product_price_whole_final.append(product_price)
        
        product_price_whole_final.sort(key=len,reverse=True)
        yield{'product_price':product_price_whole_final[0]}
        
        amazontestspider.url_number+=1
        if amazontestspider.url_number<=1:
            next_url=urls[amazontestspider.url_number]
            yield response.follow(next_url,callback=self.parse)

        
            

