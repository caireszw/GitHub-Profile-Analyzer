import requests
import json


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
            print('passou')
        
        print(f'NOME: {dados["login"]}\nBIO:{dados["bio"]}\nREPOS: {dados["public_repos"]}\nSEGUIDORES: {dados["followers"]}\nSEGUINDO: {dados["following"]}\nDATA DE CRIAÇÃO: {dados["created_at"]}')
    
    else: 
        print('Requisição Invalida erro na api!')
    

def repositorios_user():
    user = str(input('Digite o usuario: '))

    link_api_reps = f"https://api.github.com/users/{user}/repos"
    requisicao_api = requests.get(link_api_reps)
    dados = requisicao_api.json()
    
    with open('repositorios.json','w',encoding='utf-8') as arq:
        json.dump(dados,arq,ensure_ascii=False,indent=4)



repositorios_user()