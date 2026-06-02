import interface
import consultas
from time import sleep
from rich import print

import interface

while True:
    interface.menu('Consultar Usuario','Consultar Repositorios','Ver Historico','Comparar Usuarios','Apagar Historico','[red]SAIR DO PROGRAMA[/]')
    opc1 = interface.selecionar_opcao('Digite a opção desejada: ')
    if opc1 == 1:
        consultas.adicionar_user()
    elif opc1 == 2:
        consultas.repositorios_user()
    elif opc1 == 3:
        consultas.verhistorico()
    elif opc1 == 4:
        consultas.compararuser()
    elif opc1 == 5:
        while True:
            opc2 = interface.selecionar_opcao('DESEJA APAGAR O HISTORICO [1-SIM] [2-NÃO]')
            if opc2 == 1:
                consultas.apagarhistorico()
                break
            elif opc2 == 2:
                print('RETORNANDO AO MENU')
                break
            else:
                print('opção invalida')
    elif opc1 == 6:
        print('FIM DO SISTEMA OBRIGADO!')
        break
    elif opc1 > 6:
        print('Opção Invalida!')   
    sleep(2)