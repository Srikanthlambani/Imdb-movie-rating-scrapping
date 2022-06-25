from bs4 import BeautifulSoup
import requests
import pandas as pd
names=[]
years=[]
ratings=[]
r=requests.get("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc").text
soup=BeautifulSoup(r,'lxml')
for ait in soup.findAll('div',attrs={'class':'lister-item mode-advanced'}):
    name=ait.h3.a.text
    year=ait.find('span',attrs={'class':'lister-item-year text-muted unbold'}).text
    rate=ait.find('div',attrs={'class':'inline-block ratings-imdb-rating'}).strong.text
    names.append(name)
    years.append(year)
    ratings.append(rate)
df=pd.DataFrame({'mOVIE NAme':names,'year':years,'ratings':ratings})
df.to_csv('srikanth_movie_ratings.csv',index=False,encoding='utf-8')
print('success')
