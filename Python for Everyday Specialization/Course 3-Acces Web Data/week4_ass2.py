import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

#Ignore SSL certificate errors / Secure Socket Layers
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

i = 0
last = 'http://py4e-data.dr-chuck.net/known_by_Adalaide.html'
while i < 7: #Do it for 7 times
    i += 1
    html = urllib.request.urlopen(last, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    positions = soup('a')
    taken = list()

    #Just look and add until 18. link
    for position in positions[:18]:
        taken.append(position.get('href', None))
        
    last = taken[17] #Take 18. link to use

last_guy = re.findall('by_(.*).h', last) #Find the name wit regular expressions via last line
print(last_guy[0])
