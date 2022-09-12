import urllib.request, urllib.error, urllib.parse
import xml.etree.ElementTree as ET
import ssl

#Ignore SSL certificate errors / Secure Socket Layers
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Take url and read with 'urllib'
myxml = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1584316.xml', context=ctx).read()

#Look comment tags under comments, add them a list
stuff = ET.fromstring(myxml) 
lst = stuff.findall('comments/comment')

#Create a list, look text inside count tags
#Convert str to int before add 
numbers = list()
for item in lst:
    i = item.find('count').text
    i = int(i)
    numbers.append(i)

#Sum of all numbers items
print(sum(numbers))