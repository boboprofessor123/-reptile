import bs4
import requests
import time
import urllib3
import re
from selenium import webdriver

all_information = []
driver = webdriver.Chrome('./chromedriver')
driver.get('https://kma.kkbox.com/charts/hourly?terr=tw&lang=tc#') #高鐵網站
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
soup = bs4.BeautifulSoup(driver.page_source, 'html.parser') #解析html

song_singer = soup.select("body > div.container > div > div.col-12.col-md-9 > ul > li > a > div > div.flipper-item.layer1 > span.charts-list-desc > span.charts-list-artist")
song_name = soup.select("body > div.container > div > div.col-12.col-md-9 > ul > li > a > div > div.flipper-item.layer1 > span.charts-list-desc > span.charts-list-song")
rank = soup.select("body > div.container > div > div.col-12.col-md-9 > ul > li > a > span.charts-list-rank")
date = soup.select("body > div.container > div > div.col-12.col-md-9 > ul > li > a > div > div.flipper-item.layer1 > span.charts-list-date")
for i in range(0, len(rank)):
    all_information.append(rank[i].text + ' ' + song_singer[i].text + ' ' + song_name[i].text + ' ' + date[i].text)
for j in all_information:
    print(j)