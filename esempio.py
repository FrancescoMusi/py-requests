import requests
#accreditamento
requests.post("http://192.168.1.231:8080/accreditamento", json = {"nome": "Francesco Musi"})

#ottieni il dict con consegna e dati
r = requests.get("http://192.168.1.231:8080/esercizi/1").json()
#stampa consegna e dati
print(r)

#svolgimento
out = []
for i in r["data"]:
	

#manda la risposta
r = request.post("http://192.168.1.231:8080/esercizi/1", json = {"data": out})
#dice se giusto/sbagliato
print(r.json())