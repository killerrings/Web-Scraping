from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests

##Defining the url of the page
# top_url = "https://soundcloud.com/charts/top"
# new_url = "https://soundcloud.com/charts/new"
# track_url = "https://soundcloud.com/charts/search/sounds?q="
# artist_url = "https://soundcloud.com/charts/seach/people?q="
# mix_url_end = "&filter.duration=epic"
url = "https://soundcloud.com/charts/top"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

##Creating a selenium browser 
# browser = webdriver.Chrome("C:/Users/Swaraj/Downloads/chromedriver_win32/chromedriver")
# browser.get(url)

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, features="html.parser")
for menu in soup.findAll('a', class_='sc-link-dark'):
	print(menu.text)

##Creating a list of all the things we want to ectract
# track_name = []
# artist_name = []
# played_times = []

##Extracting the necessary files track name, artist name and number of plays
# content = browser.page_source
# soup = BeautifulSoup(content, 'html.parser')
# for a in soup.findAll('li', attrs={'class':'chartTracks__item'}):
# 	name = a.find('a', href=True, attrs={'class':'sc-link-dark'})
# 	artist = a.find('a',href=True, attrs={'class':'sc-link-light'})
# 	palyed = a.find('span', attrs={'class':'sc-visuallyhidden'})

# 	track_name.append(name.text)
# 	artist_name.append(artist.text)
# 	played_times.append(played.text)

# print(track_name)

#Exporting it to a CSV file 
# df = pd.DataFrame({'Track Name':track_name,'Artist Name':artist_name, 'Played (All time)':played_times})
# df.to_csv('Soundcloud.csv', index=False, encoding='utf-8')