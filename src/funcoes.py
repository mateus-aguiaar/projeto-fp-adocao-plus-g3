import src.menus as ui
from datetime import datetime,date
import csv
import os 

def cadastro_animal(escolha):
    if escolha == 1:      
        nome_animal = input("\nInforme o nome do seu animal: ").lower().capitalize()
        raca_animal = input("\nInforme a raça do seu animal: ")
        idade_animal = int(input("\nInforme a idade do seu animal: "))
        estado_saude_animal = input("\nInforme o estado de saúde do seu animal: ")
        comportamento_animal = (input("\nInforme como o seu animal se comporta: "))
        
        while True:
            chegada_animal = int(input(ui.MENU_DATA_CHEGADA))
            if chegada_animal == 1:
                data_chegada = date.today()
                data_id = datetime.now().strftime("%d%m%Y%H%M%S")
                id_animal = data_id.replace("/","")
                break

            elif chegada_animal == 2:
                while True:
                    data_final = input("Digite a data (DD/MM/AAAA): ")
                    data_chegada = data_final.replace("/","-")
                    id_animal = data_final.replace("/","")

                    if not id_animal.isdigit() or len(id_animal) != 8:
                        print("\nData inválida.")
                        continue    
                    break
                break
            else:
                os.system("cls")
                print("\033[1;31mOpção inválida\033[m") 
        try:
            arquivo_existe = os.path.exists("data/animais.csv")
            with open ("data/animais.csv", "a", newline = "", encoding = "utf-8") as arquivo:
                writer = csv.writer(arquivo)
                if not arquivo_existe:
                    writer.writerow(["id_animal", "nome", "raca", "idade", "estado_saude", "comportamento", "data_chegada"])
                writer.writerow([id_animal, nome_animal, raca_animal, idade_animal,estado_saude_animal,comportamento_animal,data_chegada])
                print("\n\033[1;32mCadastro realizado com sucesso!\033[m")
        
        except ValueError:
            print("\033[1;31mValor inválido\033[m")

        return

def verificar_animal(escolha):
    if escolha == 2:
        try:
            with open("data/animais.csv", "r", newline = "", encoding = "utf-8") as arquivo:
                reader = csv.reader(arquivo)

                nome_verificacao = input("\nQual o nome do animal: ").lower().capitalize()
                os.system("cls")
                animais_encontrados = []
                for linha in reader:
                    if nome_verificacao == linha[1]:
                        animais_encontrados.append(linha)
                while True:
                    if len(animais_encontrados) == 0:
                            print("Nenhum animal foi encontrado!")
                            break

                    elif len(animais_encontrados) == 1:
                            linha = animais_encontrados[0]
                            print(f"{'Campo':<20} {'Valor'}")
                            print("-" * 30)
                            print(f"{'Nome':<20} {linha[1]}")
                            print(f"{'Raça':<20} {linha[2]}")
                            print(f"{'Idade':<20} {linha[3]} anos")
                            print(f"{'Estado de saúde':<20} {linha[4]}")
                            print(f"{'Comportamento':<20} {linha[5]}")
                            print(f"{'Data de chegada':<20} {linha[6]}")
                            break
                    else:
                        print("\nMais de um animal com o mesmo nome:\n")
                        for i, animal in enumerate(animais_encontrados):
                            print(f"[{i+1}] {animal}")
                    try:
                        selecao_animal = int(input(ui.MENU_ESCOLHA_ANIMAL))
                        if selecao_animal < 1 or selecao_animal > len(animais_encontrados):
                            print("\nOpção inválida")   
                            continue
                        else:   
                            linha = animais_encontrados[selecao_animal - 1] 
                            os.system("cls")
                            print(f"{'Campo':<20} {'Valor'}")
                            print("-" * 30)
                            print(f"{'Nome':<20} {linha[1]}")
                            print(f"{'Raça':<20} {linha[2]}")
                            print(f"{'Idade':<20} {linha[3]} anos")
                            print(f"{'Estado de saúde':<20} {linha[4]}")
                            print(f"{'Comportamento':<20} {linha[5]}")
                            print(f"{'Data de chegada':<20} {linha[6]}")
                            break
                    except ValueError:
                        print("\nDigite um número válido.")
        except FileNotFoundError:
            print("\033[1;31mNenhum animal cadastrado\033[m")

def atualizar_animal (escolha):
    if escolha == 3:
        with open ("data/animais.csv", "r", newline = "", encoding = "utf-8" ) as arquivo:
            reader = csv.reader(arquivo)

            while True:
                cpf_dono = input("\nInforme o seu CPF, nesse padrão 356.314.567-80: ")
                cpf_limpo = cpf_dono.replace(".", "").replace("-", "")

                if cpf_limpo.isdigit() == False:
                    print("CPF Inválido, digite apenas números.")

                else:
                    if len(cpf_limpo) != 11:
                        print("CPF incompleto.")

                    else:
                        cpf_formatado = cpf_limpo[0:3] + "." + cpf_limpo[3:6] + "." + cpf_limpo[6:9] + "-" + cpf_limpo[9:12]
                        print(cpf_formatado)
                        z