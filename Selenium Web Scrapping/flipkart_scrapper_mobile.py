from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

##Sepcifying link from which extraction to be made
url = "https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

##Creating a selenium website for Flipkart mobiles section
browser = webdriver.Chrome('C:/Users/Swaraj/Downloads/chromedriver_win32/chromedriver')
browser.get(url)

##Creating a list of what we need to extract
mobiles = []
prices = []
ratings =[]

##Extracting the files
content = browser.page_source
soup = BeautifulSoup(content, 'html.parser')
for a in soup.findAll('a', href = True, attrs={'class' : '_31qSD5'}):
	name = a.find('div', {'class':'_3wU53n'})
	price = a.find('div', {'class':'_1vC4OE _2rQ-NK'})
	rating = a.find('div', {'class':'hGSR34'})

	mobiles.append(name.text)
	prices.append(price.text)
	ratings.append(rating.text)


##Exporting it to a CSV file 
df = pd.DataFrame({'Mobile Names':mobiles,'Prices':prices, 'Ratings':ratings})
df.to_csv('Mobiles.csv', index=False, encoding='utf-8')
