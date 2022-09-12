import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors / Secure Socket Layers
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1584314.html', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#This is for dedicate the true part for 'for loop'.
"""
# Retrieve all of the td tags. I found it from page 'incele'
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
"""

sum = 0
#Take all the contents
tags = soup('span')
for tag in tags:
    sum = sum + int(tag.contents[0])
    
print(sum)   