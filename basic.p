#!/usr/bin/env python3
import request
url = "https://postman-echo.com/basic/auth"
user = "postman"
password = "password"
r = request.get (url.auth=(user,password))
print (r.status_code)
print (r.jason())
