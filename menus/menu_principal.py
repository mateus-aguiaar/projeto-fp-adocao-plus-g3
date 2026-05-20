# Criar um menu na qual vamos escolher, adicionar, vizualizar, atualizar e deletar.
from datetime import date
import csv
MENU_PRINCIPAL = """
[1] Adicionar animais
[2] Verificar animais
[3] Atualizar animais
[4] Deletar animais

Qual opção você deseja: """

MENU_DATA_CHEGADA = """ 
[1] Utilizar data de hoje
[2] Digitar a data manualmente 

Qual opção você deseja: """

MENU_SAIDA = """
[1] continuar
[2] 

Qual opção você deseja: """

def cadastro_animal(escolha):
    if escolha == 1:
        nome_do_animal = input("\nInforme o nome do seu animal: ")
        raca_do_animal = input("\nInforme a raça do seu animal: ")
        idade_do_animal = int(input("\nInforme a idade do seu animal: "))
        estado_saude_animal = input("\nInforme o estado de saúde do seu animal: ")
        comportamento_do_animal = (input("\nInforme como o seu animal se comporta: "))
        chegada_animal = int(input(MENU_DATA_CHEGADA))
        if chegada_animal == 1:
            data_final = date.today()
        elif chegada_animal == 2:
            data_final = input("Digite a data (DD/MM/AAAA)")
        with open ("data/animais.csv", "a", newline = "", encoding = "utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow([nome_do_animal, raca_do_animal, idade_do_animal,estado_saude_animal,comportamento_do_animal,data_final])
            print("\n\033[1;32mCadastro realizado com sucesso!\033[m")
    return