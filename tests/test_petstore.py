import requests
import pytest


URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'a049ed076921463da9911d635fe90816'
HEADER = {'Content-Type' : 'application/json'}
HEADERS = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '4052'


def test_status_code_trainers():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200
    
def test_status_code_pokemons():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
    
def test_part_of_response_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Juker'

def test_part_of_response_poke_name():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Бульбазавр'
    
@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'),('trainer_id', TRAINER_ID),('id', '26951')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value