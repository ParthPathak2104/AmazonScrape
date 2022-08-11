import pandas as pd
import numpy as np

#change path according to your directory structure

# def generateurls():
path="C:/Parth/Study Material/Web Development/scrappy/amazon/Amazon Scraping - Sheet1.csv"

df=pd.read_csv(path,nrows=100)

# urlstype1=[]
# urlstype2=[]
def generateurls(a,b):
    urls=[]
    for i in range(a,b):

        asin=df.loc[i]['Asin']
        country=df.loc[i]['country']
        
        url="https://www.amazon.{x}/dp/{y}".format(x=country,y=asin)
        urls.append(url)

        # if len(asin)>=4 and int(asin[3])==0 and asin[-1]=='X' :
        #     urlstype1.append(url)
        # else:
        #     urlstype2.append(url)

    return urls

# urlstobeused=generateurls()
# print(urlstobeused)

