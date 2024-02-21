import requests, json

new_car = {	'id': 5,
		'brand': 'auto',
		'model': 'xxx',
		'production_year': 2500,
		'convertible': False}
adat = json.dumps(new_car)
header = {"Content-Type":"application/json"}
try:
	reply = requests.put("http://localhost:3000/cars/5", headers=header, data=adat)
except:
	print("Halozati hiba!")
	exit()
print(reply.status_code)


