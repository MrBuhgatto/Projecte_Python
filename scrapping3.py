import requests

def inf_range():
	num = 1
	while True:
		yield num
		num +=1

for e in inf_range():
	a = "https://pokeapi.co/api/v2/pokemon/"+str((e+1))
	res=requests.get(a)
	if res.status_code == 200:
		dades = res.json()
		print("El nom del pokémon és: {}".format(dades["species"]["name"]))
else:
	print("No hi ha dades.")
