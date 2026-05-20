import menus.menu_principal as ui
import os
from datetime import date
os.system("cls")

while True:
    escolha = int(input(ui.MENU_PRINCIPAL))
    if escolha == 1:
        ui.cadastro_animal(escolha)
    opcao = int(input(ui.MENU_SAIDA))
    if opcao == 1:
        os.system("cls")
        continue
    elif opcao == 2:
        break
    else:
        print("\033[1;31mOpção inválida\033[m")