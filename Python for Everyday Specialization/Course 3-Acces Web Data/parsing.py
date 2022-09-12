import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter: ')
#http://www.dr-chuck.com/page1.htm use this one

html = urllib.request.urlopen(url).read() #Type: bytes /// It reads all together and get a big string
soup = BeautifulSoup(html, 'html.parser') 

#Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
