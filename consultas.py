import requests
import json
from rich import print


def lin():
    print('-'*30)

def adicionar_user():

    user = str(input('Digite o nome do usuario: '))

    link_api = f'https://api.github.com/users/{user}'
    requisicao_api = requests.get(link_api)
    dados =  requisicao_api.json()

    if requisicao_api.status_code == 200:

        with open('users.json','r',encoding='utf-8') as arq:
            lista = json.load(arq)

        with open('users.json','w',encoding='utf-8') as arq:
            lista.append(dados)
            json.dump(lista,arq,ensure_ascii=False,indent=4)
            print('adicionado')
        
        print(f'NOME: {dados["login"]}\nBIO:{dados["bio"]}\nREPOSITORIOS: {dados["public_repos"]}\nSEGUIDORES: {dados["followers"]}\nSEGUINDO: {dados["following"]}\nDATA DE CRIAÇÃO: {dados["created_at"]}')
    
    else: 
        print('Requisição Invalida erro na api!')
    

def repositorios_user():
    user = str(input('Digite o usuario: '))

    link_api_reps = f"https://api.github.com/users/{user}/repos"
    requisicao_api = requests.get(link_api_reps)
    dados = requisicao_api.json()
    

    contador = 1
    lin()
    print(f'USUARIO: {user}')
    lin()
    for item in dados: 
        print(f'{contador}-{item["name"]}')
        contador += 1
    lin()
   


def verhistorico():
    with open('users.json','r',encoding='utf-8') as arq:
        dados = json.load(arq)

    contador = 1 
    for item in dados:
        print(f'CONSULTA {contador} - {item["login"]}')
        contador += 1 



def compararuser():
    with open('users.json', 'r', encoding='utf-8') as arq:
        dados = json.load(arq)

    lin()
    for pessoa in dados:
        print(pessoa["login"])
    lin()

    while True:
        usuario1 = None
        usuario2 = None

        user1 = input('Digite o usuário que deseja comparar: ')
        user2 = input('Digite o outro usuário que deseja comparar: ')

        for pessoa in dados:
            if pessoa["login"] == user1:
                usuario1 = pessoa

            if pessoa["login"] == user2:
                usuario2 = pessoa

        if usuario1 and usuario2:
            print(
                f'{usuario1["login"]} possui {usuario1["followers"]} seguidores '
                f'e {usuario1["public_repos"]} repositórios X '
                f'{usuario2["login"]} possui {usuario2["followers"]} seguidores '
                f'e {usuario2["public_repos"]} repositórios'
            )
            break
        else:
            print('[red]Usuários não encontrados, tente novamente![/]')


def apagarhistorico():
    with open('users.json','w') as arq:
        json.dump([],arq)
        print('HISTORICO LIMPO!')



