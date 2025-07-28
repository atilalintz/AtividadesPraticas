import requests

response = requests.get('https://randomuser.me/api/?nat=br')

if response.status_code == 200:
    data = response.json()['results'][0]
    nome = data['name']['first'] + ' ' + data['name']['last']
    email = data['email']
    pais = data['location']['country']
    print(nome, email, pais)
else:
    print('Erro na requisição:', response.status_code)


