from email import header
from itertools import count
import urllib.request, urllib.error, urllib.parse
from twurl import augment
import ssl

#https://apps.twitter.com/
#Create App and get four strings, put them in hidden.py

print('*Calling Twitter...')

url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
              {'screen_name': 'drchuck', 'count':2}  )
print(url)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read()
print(data)

print('==============================')
headers = dict(connection.getheaders())
print(headers)