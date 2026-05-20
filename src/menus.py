# Criar um menu na qual vamos escolher, adicionar, vizualizar, atualizar e deletar.
from datetime import date
import csv
import os 
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
[2] sair

Qual opção você deseja: """

def cadastro_animal(escolha):
    if escolha == 1:
        while True:
            cpf_dono = input("\nInforme o seu CPF, nesse padrão 356.314.567-80: ")
            if len(cpf_dono) != 11:
                print("CPF incompleto.")
                continue
            else:
                break
        cpf_formatado = cpf_dono[0:3] + "." + cpf_dono[3:6] + "." + cpf_dono[6:9] + "-" + cpf_dono[9:12]
        nome_do_animal = input("\nInforme o nome do seu animal: ").lower()
        raca_do_animal = input("\nInforme a raça do seu animal: ")
        idade_do_animal = int(input("\nInforme a idade do seu animal: "))
        estado_saude_animal = input("\nInforme o estado de saúde do seu animal: ")
        comportamento_do_animal = (input("\nInforme como o seu animal se comporta: "))
        while True:
            chegada_animal = int(input(MENU_DATA_CHEGADA))
            if chegada_animal == 1:
                data_final = date.today()
                break
            elif chegada_animal == 2:
                data_final = input("Digite a data (DD/MM/AAAA): ")
                break
            else:
                os.system("cls")
                print("\033[1;31mOpção inválida\033[m")
        try:
            arquivo_existe = os.path.exists("data/animais.csv")
            with open ("data/animais.csv", "a", newline = "", encoding = "utf-8") as arquivo:
                writer = csv.writer(arquivo)
                if not arquivo_existe:
                    writer.writerow(["cpf", "nome", "raca", "idade", "estado_saude", "comportamento", "data_chegada"])
                writer.writerow([cpf_formatado,nome_do_animal, raca_do_animal, idade_do_animal,estado_saude_animal,comportamento_do_animal,data_final])
                print("\n\033[1;32mCadastro realizado com sucesso!\033[m")
        except ValueError:
            print("Valor inválido")
    return
def verificar_animal(escolha):
    if escolha == 2:
        try:
            with open("data/animais.csv", "r", newline = "", encoding = "utf-8") as arquivo:
                reader = csv.reader(arquivo)
                nome_verificacao = input("\nQual o nome do animal: ").lower()
                while True:
                    cpf_cadastro = input("\nQual o seu CPF: ")
                    if len(cpf_cadastro) != 11:
                        print("\nCPF incompleto.")
                        continue
                    else:
                        break
                cpf_cadastro_formatado = cpf_cadastro[0:3] + "." + cpf_cadastro[3:6] + "." + cpf_cadastro[6:9] + "-" + cpf_cadastro[9:12]
                animal_encontrado = False
                for linha in reader:
                    if cpf_cadastro_formatado == linha[0] and nome_verificacao == linha[1]:
                        animal_encontrado = True
                        print(f"\nNome: {linha[1]}")
                        print(f"\nRaça: {linha[2]}")
                        print(f"\nIdade: {linha[3]} anos.")
                        print(f"\nEstado do animal: {linha[4]}")
                        print(f"\nComportamento: {linha[5]}")
                        print(f"\nData de chegada do animal: {linha[6]}")
                if not animal_encontrado:
                    print("\n\033[1;31mAnimal não encontrado!\033[m")
        except FileNotFoundError:
            print("\033[1;31mNenhum animal cadastrado\033[m")