#!/usr/bin/env python3
import requests
from requests.auth import HTTPDigestAuth

url = "https://httpbin.org/digest-auth/auth/user/pass"
user = "user"
password= "pass"
try:
        r = requests.get(url, auth=HTTPDigestAuth(user, password)) 
except:
        print("Halozati hiba!")
        exit()
print(r.status_code)
print(r.json())
