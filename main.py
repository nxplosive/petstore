import requests


URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'a049ed076921463da9911d635fe90816'
HEADER = {'Content-Type' : 'application/json'}
HEADERS = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '4052'
BODY_REG = {
    "trainer_token": TOKEN,
    "email": "121212@ya.ru",
    "password": "blahBlah1"
}
BODY_CONFIRMATION = {
    "trainer_token": TOKEN
}
BODY_CREATE = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
BODY_CHANGE_NAME = {
    "pokemon_id": "26935",
    "name": "Avangardo",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
BODY_ADD_POKEBALL = {
    "pokemon_id": "26935"
}
BODY_BATTLE = {
    "attacking_pokemon": "26935",
    "defending_pokemon": "26925"
}

# Регистрация тренера
response_trainer_reg = requests.post(url= f'{URL}/trainers/reg', headers= HEADER, json= BODY_REG)
print(response_trainer_reg.text)

# Подтверждение почты
response_confirmation_email = requests.post(url= f'{URL}/trainers/confirm_email', headers= HEADER, json= BODY_CONFIRMATION)
print(response_confirmation_email.text)

# Создание покемона
response_create = requests.post(url= f'{URL}/pokemons', headers= HEADERS, json= BODY_CREATE)
print(response_create.status_code)
pokemon_id = response_create.json()["id"]
print(pokemon_id)
message = response_create.json()["message"]
print(message)

# Получение списка тренеров
response_trainer_list = requests.get(url= f'{URL}/trainers')
print(response_trainer_list.text)

# Смена имени покемона
response_change_name = requests.put(url= f'{URL}/pokemons', headers= HEADERS, json= BODY_CHANGE_NAME)
print(response_change_name.json())

# Поймать покемона в покебол
response_add_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers= HEADERS, json= BODY_ADD_POKEBALL)
print(response_add_pokeball.json())

# Получение ID всех активных покемонов с уровнем 1
response_opponent = requests.get(url= f'{URL}/pokemons?in_pokeball=1&attack=1')
oppo_id = response_opponent.json()["data"]
dsa = len(oppo_id) # Количество всех айди
asd = 0 # Переменная int отвечающая за вывод текущего айди (т.е. индекс)
print("Всего айдишников: ", dsa)
while(True): #Бесконечный цикл
    if asd==dsa: # Если asd равняется количеству всех айди dsa, то цикл обрывается
        break
    print(oppo_id[asd]["id"]) # Вывод айди с индексом asd
    asd+=1 # Прибавление единицы к текущему индексу asd

# Провести битву покемонов
response_battle = requests.post(url= f'{URL}/battle', headers= HEADERS, json= BODY_BATTLE)
print(response_battle.json())

# Выселить покемона из покебола
response_delete_pokeball = requests.put(url= f'{URL}/trainers/delete_pokeball', headers= HEADERS, json= BODY_ADD_POKEBALL)
print(response_delete_pokeball.json())