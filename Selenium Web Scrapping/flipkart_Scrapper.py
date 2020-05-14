##Import all necessary packages
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd

##Flipkart url we are going to scrap
url = "https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2"

##Creating a selenium page for Flipkart
browser = webdriver.Chrome('C:/Users/Swaraj/Downloads/chromedriver_win32/chromedriver')
browser.get(url)

##Creating a lost for what we need tro extract 
products = []
prices = []
ratings = []

##The data we want to extract is nested in <div> tags. So, We will find the div tags with those respective 
##class-names, extract the data and store the data in a variable.
content = browser.page_source
soup = BeautifulSoup(content, 'html.parser')
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
	name=a.find('div', attrs={'class':'_3wU53n'})
	price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
	rating=a.find('div', attrs={'class':'hGSR34'})
	products.append(name.text)
	prices.append(price.text)
	ratings.append(rating.text) 


##Extractinf data to a CSV file
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')