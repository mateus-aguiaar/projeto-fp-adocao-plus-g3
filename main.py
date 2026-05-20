import src.menus as ui
import os
os.system("cls")

while True:
    escolha = int(input(ui.MENU_PRINCIPAL))
    if escolha == 1:
        ui.cadastro_animal(escolha)
    elif escolha == 2:
        ui.verificar_animal(escolha)
    opcao = int(input(ui.MENU_SAIDA))
    if opcao == 1:
        os.system("cls")
        continue
    elif opcao == 2:
        os.system("cls")
        print("\n\033[1;31mProgama encerrado!\033[m")
        break
    else:
        print("\033[1;31mOpção inválida\033[m")