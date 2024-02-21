
import requests, json

new_car = {
            "id": 1,
            "name": "Mariadb",
            "type": "RDBMS"
}
adat = json.dumps(new_car)
header = {"Content-Type":"application/json"}
try:
                reply = requests.post("http://localhost:3000/databases", headers=header, data=adat)
except:
        print("Halozati hiba")
      	exit()

