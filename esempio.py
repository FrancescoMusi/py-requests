import requests
import os

esercizio = '30'

'''
#accreditamento
accr = requests.post("http://192.168.1.231:8080/accreditamento", json = {"nome": "Francesco Musi"})
print(accr.json())

'''
#ottieni il dict con consegna e dati
r = requests.get("http://192.168.1.231:8080/esercizi/{}".format(esercizio), headers = {"x-data": "true"})

message = r.json()['message']
data = r.json()['data']

os.system('cls')
print()
print(message)
print()
print(data)
print()

x = 0
y = 0
field = []

field = data.split('\n')
print(field)
out = []

for i in field:
	if 'X' in i:
		x = i.index('X')
		y = field.index(i)

print(x, y)

out = {
	'x': x,
	'y': y
}

#manda la risposta
res = requests.post("http://192.168.1.231:8080/esercizi/{}".format(esercizio), json = {"data": out})
print(res.json()['message'])
