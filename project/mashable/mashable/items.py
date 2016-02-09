# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#libraries below are used to process/bring in the .csv
import pandas as pd
import numpy as np


import scrapy


class MashableItem(scrapy.Item):
	
	mash_items = pd.read_csv("OnlineNewsPopularity_inscrapy.csv")
	mash_url_only = mash_items.url.head(100)
	mash_url_only = mash_url_only.tolist() #turns the series into a list

	title = scrapy.Field() #done
	h1 = scrapy.Field() #done
	author = scrapy.Field() #done

	#example labels
	description = scrapy.Field() #done
	url = scrapy.Field() #done

    # define the fields for your item here like:
    # name = scrapy.Field()
 
