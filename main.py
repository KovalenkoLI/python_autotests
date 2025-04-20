import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ce538733ca031af7ccf54186119dd75e'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
BODY_CREATION = {"name": "красти краб", "photo_id": 99}
TRAINER_ID = 29310

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CREATION)
print(response_create.text)

ID= response_create.json()['id']
print(ID)
BODY_CHANGE = {"pokemon_id": ID, "name": "New Name", "photo_id": 2}
BODY_POKEBALL = {"pokemon_id": ID}

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CHANGE)
print(response_change.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_POKEBALL)
print(response_pokeball.text)