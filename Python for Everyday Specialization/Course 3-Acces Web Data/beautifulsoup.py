import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors / Secure Socket Layers
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))

#Retrieve all the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None)) #Take just href parts from a anchors