import requests

# URL base de la API
url = "https://pokeapi.co/api/v2/pokemon"

# Inicializar variables
pokemon_list = []
next_url = url

# Función para obtener Pokémon de una URL dada
def get_pokemon(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["results"], data["next"]
    else:
        print(f"Error: {response.status_code}")
        return [], None

# Obtener Pokémon mientras haya una URL siguiente
while next_url:
    results, next_url = get_pokemon(next_url)
    pokemon_list.extend(results)

# Imprimir la lista de Pokémon
for pokemon in pokemon_list:
    print(pokemon["name"])
