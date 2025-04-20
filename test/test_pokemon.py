import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ce538733ca031af7ccf54186119dd75e'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '29310'


def test_status_code():
    response_trainers = requests.get(url = f'{URL}/trainers')
    assert response_trainers.status_code == 200
  
def test_my_trainer():
    response_my_trainer = requests.get(url = f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_my_trainer.json()['data'][0]['trainer_name'] == 'Leonidas'

@pytest.mark.parametrize('key, value', [('id', TRAINER_ID),('trainer_name', 'Leonidas'),('city', 'Челябинск')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value