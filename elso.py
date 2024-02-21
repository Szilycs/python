import requests
url = "https://cat-Jact.herokuapp.car/Facts"
try:
	reply = requests.get(url)
except:
	print("Halozati hiba!")
	exit()
print (reply.status_code)
print (reply.text)
