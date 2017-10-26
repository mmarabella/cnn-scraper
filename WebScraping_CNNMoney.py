# import libraries
try:
	from urllib.request import urlopen
except:
	from urllib2 import urlopen

from bs4 import BeautifulSoup

# specify the url
DJ_page = 'http://money.cnn.com/data/markets/dow/'
CC_page = 'http://markets.money.cnn.com/Marketsdata/Sectors/ConsumerCyclical'

# query website and return html to variable 'page'
DJ_page = urlopen(DJ_page)
CC_page = urlopen(CC_page)

# parse the html using beautiful soap and store in variable 'soup'
DJ_soup = BeautifulSoup(DJ_page, 'html.parser')
CC_soup = BeautifulSoup(CC_page, 'html.parser')

# Take out the <div> of name and get its value -- DJ
DJ_box = DJ_soup.find('span', attrs={'class': 'posData'})
DJ_change = DJ_box.text.strip() 
print (DJ_change)

CC_box = CC_soup.find('span', attrs={'class': 'span-perc-nav decreasingperc'})
CC_change = CC_box.text.strip()
print(CC_change)


import csv
from datetime import datetime

# open a csv file with append, so old data will not be erased
with open('WebScraping_CNN.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([datetime.now(), DJ_change, CC_change,])