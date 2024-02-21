import requests

szam = input("Melyiket toroljuk? ")
url = "http://localhost:3000/databases/"
try:
        print = (requests.delete(url + szam).status_code)
except:
        print("Halozati Hiba!")

