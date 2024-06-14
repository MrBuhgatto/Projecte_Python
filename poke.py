import requests

def ppokemon():
    for i in range(180):
        pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{i}/"
        response = requests.get(pokemon_url)
        
        if response.status_code == 200:
            data = response.json()
            name = data["name"]
            ability = data["abilities"][0]["ability"]["name"] if data["abilities"] else "ninguno"
            print("El nombre del Pokémon es: {}, y su habilidad es: {}".format(name,ability))
        else:
            print("No se encotraron datos.".format(i))
    print("Fin del scrapping.")