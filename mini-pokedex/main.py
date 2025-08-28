import requests

base_url = 'https://pokeapi.co/api/v2/'

def get_poke_info(nome):
    url = f'{base_url}/pokemon/{nome}'
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        pokemon_data = resposta.json()
        return pokemon_data
    else:
        print(f'Falha: {resposta.status_code}')

nome_pokemon = input('Me diga um pokémon: ')
pokemon_info = get_poke_info(nome_pokemon)

if pokemon_info:
    print(f'Name: {pokemon_info['name'].capitalize()}')
    for type in pokemon_info['types']:
        print(f'Type: {type['type']['name'].capitalize()}')
    
    for ability in pokemon_info['abilities']:
        print(f'Ability: {ability['ability']['name'].capitalize()}')
        
    print(f'ID: {pokemon_info['id']}')
    print(f'Height: {pokemon_info['height']}')
    print(f'Weight: {pokemon_info['weight']}')