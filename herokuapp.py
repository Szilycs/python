import requests
url = "https://cat-fact.herokuapp.com/facts"
#url = "172.18.255.222"
try:
        reply = requests.get(url)
except:
        print("Halozati hiba!")
        exit()
print (reply.status_code)
print (reply.text)
