#!/user/bin/env python3
import requests, json

szam = input ("Melyik kocsit kered? ")
url = "http://localhost:3000/cars/"
h1 = {"Connection":"close"}
h2 = {"Connection":"keep-alive"}
try:
	reply = requests.get(url + szam, headers=h1)
except:
	print("Hiba!")
	exit()
print (reply.status_code)
if reply.status_code == 200:
	print(reply.json())
