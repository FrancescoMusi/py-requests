import requests
import os
#20

esercizio = '29'

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



out = 1
for i in range(1, data+1):
	out *= i


print(out)
print()

#manda la risposta
res = requests.post("http://192.168.1.231:8080/esercizi/{}".format(esercizio), json = {"data": out})
print(res.json()['message'])
