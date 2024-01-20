import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '897768f5f07fc89cc27cdf2ebc8125e7'

def test_response_json():
    response = requests.post(f'{host}/pokemons', json = { 
        "name": "BestKilahh",
        "photo": "https://dolnikov.ru/pokemons/albums/001.png"}, 
        headers = {'trainer_token' : token, 'Content-Type' : 'application/json'})
    
    
    assert response.json()





def test_response_200():
    response = requests.get(f'{host}/trainers', headers = {'Content-Type' : 'application/json'}, params = {'level' : '5', 'page' : '1'})


    assert response.status_code == 200




def test_response_trainer_id():
    response = requests.get(f'{host}/trainers', headers = {'Content-Type' : 'application/json'}, params = {'trainer_id' : '3447'})


    assert response.json()['trainer_name'] == 'Matckan'







