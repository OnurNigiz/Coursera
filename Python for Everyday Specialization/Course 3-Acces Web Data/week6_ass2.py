import urllib.parse, urllib.request, urllib.error
import json, ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Stroring the given parameters
api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"
# sample_address = "South Federal University"
data_address = input("Enter location: ")
address_wanted = data_address

params = {"address": address_wanted, "key": api_key}
paramsurl = urllib.parse.urlencode(params)

url = serviceurl.strip() + paramsurl.strip()

print('Retrieving ', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved ', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

place_id_ = js["results"][0]["place_id"]
print("place_id: ", place_id_)