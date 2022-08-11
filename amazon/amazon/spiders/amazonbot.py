#File Import
import scrapy
from urlgenerator import generateurls
from ..items import AmazonItem


#This is the function to generate urls from the csv file given in the etst document
#To change the range of rows for which we want to scrape information ,We have to change-
# a and b to the respective row numbers
#Note- row one in csv file is a=0

a=0
b=100
urls=generateurls(a,b)


class AmazonbotSpider(scrapy.Spider):
    name = 'amazonbot'
    start_urls = [
        urls[a]
    ]
    url_number=a
    handle_httpstatus_list = [404]

    def parse(self, response):
        
        #TO link to items and make a container
        items=AmazonItem()


        #This condition checks if the page is returning 404 status code
        #If the page does so the following values are yielded

        if response.status == 404:
            product_title='Not available'
            product_price_whole_final_use='Not Available'
            product_price_fraction='Not Available'
            product_image_url='Not Available'
            product_details_tags_modified='Not Available'
            product_details_tags_values='Not Available'
        
        #If status code is not 404


        else:
            #PRODUCT TITLE-common for all types of pages
            product_title=response.css("span#productTitle::text").extract_first()
            product_title=product_title.replace(u" ","")

            x=list(map(str,urls[AmazonbotSpider.url_number].split('/')))
            urlasin=x[-1]

            #Statement to differentiate between physical product urls and online product urls
            if len(urlasin)>=4 and int(urlasin[3])==0 and urlasin[-1]=='X' :
            
                product_price_whole_final_use=response.css("span.a-price-whole::text").extract_first()
                product_price_fraction=response.css("span.a-price-fraction::text").extract_first()
                product_image_url=response.css("img#landingImage::attr(src)").extract_first()
                product_details_tags_modified=response.css("#productOverview_feature_div .a-text-bold").css("::text").extract()
                product_details_tags_values=response.css(".a-span9 .a-size-base").css("::text").extract()
            

                
            else:
                #PRODUCT IMAGE URL
                product_image_url=response.css("img#imgBlkFront::attr(src)").extract_first()
                
                #PRODUCT PRICE
                #to get the price in Proper Format because there were two types of rpice fields in different pages
                product_price_whole=response.css("a.a-button-text span.a-color-base").css("::text").extract()
                product_price_whole_final=[]
                for product_price in product_price_whole:
                    product_price=product_price.replace(u"\n",u"")
                    product_price=product_price.replace(u" ",u"")
                    product_price=product_price.replace(u"\xa0€",u"")
                    product_price_whole_final.append(product_price)
        
                product_price_whole_final.sort(key=len,reverse=True)
                product_price_whole_final_use=product_price_whole_final[0]
                product_price_fraction='00'
                
                #DESCRIPTION TAGS
                #to get the detilas tags in Proper Format
                
                product_details_tags_values=response.css("#detailBullets_feature_div .a-text-bold+ span").css("::text").extract()
                product_details_tags=response.css("#detailBulletsWrapper_feature_div #detailBullets_feature_div .a-text-bold").css("::text").extract()
                product_details_tags_modified=[]
                for details_tags in product_details_tags:
                    details_tags=details_tags.replace(u"\u200f\n",u"")
                    details_tags=details_tags.replace(u"\u200e\n",u"")
                    details_tags=details_tags.replace(u"\n",u"")
                    details_tags=details_tags.replace(u":",u"")
                    details_tags=details_tags.replace(u" ",u"")
                    product_details_tags_modified.append(details_tags)
            

        #yield {'product_title':product_title,'product_price_whole':product_price_whole_final_use,'product_price_fraction':product_price_fraction,'product_image_url':product_image_url,'product_detail_tags':product_details_tags_modified,'product_details_tags_values':product_details_tags_values}
        
        items['product_details_tags_values']=str(product_details_tags_values)
        items['product_details_tags']=str(product_details_tags_modified)
        items['product_image_url']=product_image_url
        items['product_price_fraction']=product_price_fraction
        items['product_price_whole']=product_price_whole_final_use
        items['product_title']=product_title
        
        yield items
        
        #This piece code runs the fnction for the next url
        AmazonbotSpider.url_number+=1
        if AmazonbotSpider.url_number<=(b-a-1):
            next_url=urls[AmazonbotSpider.url_number]
            yield response.follow(next_url,callback=self.parse)

        