import src.menus as ui
import src.funcoes as fn
import os
os.system("cls")

while True:
    escolha = int(input(ui.MENU_PRINCIPAL))
    if escolha == 1:
        fn.cadastro_animal(escolha)
    elif escolha == 2:
        fn.verificar_animal(escolha)
    elif escolha == 3:
        fn.atualizar_animal(escolha)
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