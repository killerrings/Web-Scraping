import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

##Defining the url to extract
url ='https://killerrings.github.io/SwarajGogoi/datascipro.html'

##Create a selenium webpage for my website
browser = webdriver.Chrome('C:/Users/Swaraj/Downloads/chromedriver_win32/chromedriver')
browser.get(url)

##Creating a list of the files you need to extract
projects = []
technologies = []

##Extracting files
content = browser.page_source
soup = BeautifulSoup(content, 'html.parser')
for each in soup.findAll('div', attrs={'class':'card'}):
	name = each.find('h5', attrs={'class':'card-title'})
	techs = each.find('p', attrs={'class':'alert alert-warning'})

	projects.append(name.text)
	technologies.append(techs.text)

##Exporting in a CSV format
df = pd.DataFrame({'Projects':projects,'Technologies Used':technologies})
df.to_csv('Projects.csv', index=False, encoding='utf-8')

