import requests

try:
	print = (requests.delete("http://localhost:3000/cars/6").status_code)
except:
	print("Halozati Hiba!")



