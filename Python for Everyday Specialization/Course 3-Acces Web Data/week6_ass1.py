import urllib.parse, urllib.request, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Take url from user
serviceurl = input('Enter location: ')
print('Retrieving ', serviceurl)
uh = urllib.request.urlopen(serviceurl)
data = uh.read().decode()

print('Retrieved', len(data), 'characters')

#Read json file
try:
    js = json.loads(data)
except:
    js = None

#How many comments are there
print('Count: ',len(js['comments']))

#Sum of counts
numbers = list()
for i in range(len(js['comments'])):
    a = js['comments'][i]['count']
    numbers.append(a)

print('Sum: ', sum(numbers))


