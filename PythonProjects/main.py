import requests

host = 'https://api.pokemonbattle.me:9104'
token = '897768f5f07fc89cc27cdf2ebc8125e7'





response = requests.post(f'{host}/pokemons', json = { 
        "name": "BestKilahh",
        "photo": "https://dolnikov.ru/pokemons/albums/001.png"}, 
        headers = {'trainer_token' : token, 'Content-Type' : 'application/json'})

print(response.json())




response = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "28098",
    "name": "FatalityPig",
    "photo": "https://dolnikov.ru/pokemons/albums/915.png"
}, 
        headers = {'trainer_token' : token, 'Content-Type' : 'application/json'})

print(response.json())




response = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "28098"
}, 
        headers = {'trainer_token' : token, 'Content-Type' : 'application/json'})

print(response.json())





response = requests.get(f'{host}/trainers', headers = {'Content-Type' : 'application/json'}, params = {'level' : '5', 'page' : '2'})

print(response.json())




