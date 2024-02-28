#!/user/bin/env python3
import requests, json

url = "https://172.17.255.122/restconf/"
h1 = {"Accept":"application/yang-data+json"}

try:
	reply = requests.get(url, headers=h1, verify=False, auth = ('admin', 'admin'))
except:
	print("Hiba!")
	exit()
print (reply.status_code)
if reply.status_code == 200:
	print(reply.json())
