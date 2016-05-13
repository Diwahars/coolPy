#! /usr/bin/python3

import requests
from bs4 import BeautifulSoup

city = input('Enter city: ')
url = 'http://in.bookmyshow.com/'+city
source_code = requests.get(url)
soup = BeautifulSoup(source_code.text,'lxml')

book_movie = []
i = 1
for movie_name in soup.findAll('a',{'class':'__movie-name'}):
    print (str(i)+'. '+movie_name.text)
    i += 1
    book_movie.append('http://in.bookmyshow.com'+movie_name.get('href'))

print ('Select movie no.')
movie_no = int(input())

url = book_movie[movie_no - 1]
print url
source_code = requests.get(url)
print source_code
soup = BeautifulSoup(source_code.text,'lxml')
print soup
div = soup.select('.timing')
print div
print (div[0].text)