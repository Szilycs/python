import requests, json

new_car = {	'id': 1,
		'brand': 'ferrari',
		'model': '9976',
		'production_year': 1900,
		'convertible': False}
adat = json.dumps(new_car)
header = {"Content-Type":"application/json"}
try:
	reply = requests.post("http://localhost:3000/cars", headers=header, data=adat)
except:
	print("Halozati hiba")
	exit()
print(reply.status_code)


