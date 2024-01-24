#!/usr/bin/env python3
import requests
from requests.auth import HTTPDigestAuth
url = "https://postman-echo.com/basic-auth"
user = "postman"
passw = "password"
try:
	r = requests.get (url, auth=HTTPDigestAuth(user,passw))
except:
	print ("halozati hiba")
	exit
print ("r.status code:", r.status_code)
print (r.jason())
