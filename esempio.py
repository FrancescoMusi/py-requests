import requests

requests.post("http://192.168.1.231:8080/accreditamento", json = {"nome": "Francesco Musi"})

r = requests.get("http://192.168.1.231:8080/esercizi/1").json()
print(r)

out = []
for i in r["data"]:
	#svolgimento

r = request.post("http://192.168.1.231:8080/esercizi/1", json = {"data": out})
print(r.json())