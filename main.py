import interface
import consultas
from time import sleep

import interface

while True:
    interface.menu('Consultar Usuario','Consultar Repositorios','Ver Historico','Comparar Usuarios','Apagar Historico','[red]SAIR DO PROGRAMA[/]')
    opc1 = interface.selecionar_opcao('Digite a opção desejada: ')
    if opc1 == 1:
        consultas.adicionar_user()
    elif opc1 == 2:
        consultas.repositorios_user()
    elif opc1 == 3:
        print('a')
    elif opc1 == 4:
        print('a')
    elif opc1 == 5:
        print('a')
    elif opc1 == 6:
        print('FIM DO SISTEMA OBRIGADO!')
        break
    elif opc1 > 6:
        print('Opção Invalida!')   
    sleep(2)