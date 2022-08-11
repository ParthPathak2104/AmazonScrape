# AmazonScrape
Scraping amazon website for various urls

--REQUIREMENTS--
1.scrapy
2.pandas
3.numpy

I have used scrapy to scrape the various urls'
I have done the scraping using one spider only-
  name-amazonbot
 
 to run the spyder use command-scrapy crawl amazonbot
 
 --APPROACH--
 
 --URLGENERATION--
 
 1.I have generated urls in urlgenerator.py file
 2. See file for logic
 
 --SCRAPING--
 
 1. I found out that there are 4 types of links thata are generated 
  1. the first type is 404 error
  2. the second type is a physical product page
  3.the third type is an online product page eg e-books
  4. a subtype of th eonline product page is there which has product not in stock
 
 2.  The difference between 404 page is simple as status code is 404
 3.  I differentiated between the physical product page and online product page by the asin value-
    1. The asin value of physical product page ends with an X and has 0 at the fourt position o fthe asin value(index=3)
    2. the asin value of the online product page ends with an 'X' and has a number greater than 0 at the 4 th position of asin value(index=3)
 4. The difference of pages told in [1][4] was taken care of by using replace and other python logic that can be in the amazonbot.py script
 5. 
 The json file is named -amazon.json
 
 --DATABASE---
 1. I have connected SQLITE3 
 2. Everytime the spider is run , the database is created and old database is deleted
 
 

