import src.menus as ui
from datetime import datetime,date
import csv
import os 
import random

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
                data_hoje = date.today()
                data_chegada = data_hoje.strftime("%Y-%m-%d")
                id_animal = datetime.now().strftime("%d%m%Y%H%M%S")
                break

            elif chegada_animal == 2:
                while True:
                    data_final = input("Digite a data (DD/MM/AAAA): ")
                    id_animal = data_final.replace("/","")
                    if not id_animal.isdigit() or len(id_animal) != 8:
                        print("\nData inválida.")
                        continue
                    dia,mes,ano = data_final.split("/")
                    data_chegada = f"{ano}-{mes}-{dia}"
                    id_animal = datetime.now().strftime("%d%m%Y%H%M%S")
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
                            print("-" * 30)
                            print(f"{'Nome':<20} {linha[1]}")
                            print(f"{'Raça':<20} {linha[2]}")
                            print(f"{'Idade':<20} {linha[3]} anos")
                            print(f"{'Estado de saúde':<20} {linha[4]}")
                            print(f"{'Comportamento':<20} {linha[5]}")
                            print(f"{'Data de chegada':<20} {linha[6]}")
                        
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
                                print("-" * 30)
                                print(f"{'Nome':<20} {linha[1]}")
                                print(f"{'Raça':<20} {linha[2]}")
                                print(f"{'Idade':<20} {linha[3]} anos")
                                print(f"{'Estado de saúde':<20} {linha[4]}")
                                print(f"{'Comportamento':<20} {linha[5]}")
                                print(f"{'Data de chegada':<20} {linha[6]}")
                        
                        except ValueError:
                            print("\nDigite um número válido.")
                    
                    funcionarios = ["Mateus Davi","Lucas Calixto","João Vitor","Maria Giulia", "Jullya Medeiros"]

                    gerenciar_animal = int(input(ui.MENU_GERENCIAR_ANIMAL))

                    if gerenciar_animal == 1:
                        pass
                    elif gerenciar_animal == 2:
                        tarefa = input("\nInforme a tarefa deseja para o animal: ")
                        data_tarefa = input("\nInforme a data para a tarefa: ")
                        sorteado = random.choice(funcionarios)
                        responsavel_tarefa = sorteado
                        print(f"\nO funcionário responsável pela tarefa é {responsavel_tarefa}.")
                        
                        with open("data/agendamentos.csv", "a", newline = "", encoding = "utf-8") as arquivo:
                            writer = csv.writer(arquivo)
                            writer.writerow([tarefa,data_tarefa,responsavel_tarefa])
                            break
                    else:
                        os.system("cls")
                        break

        except FileNotFoundError:
            print("\033[1;31mNenhum animal cadastrado\033[m")

def editar_info(animal_escolhido):
    while True:
        print(f"\nInformações de {animal_escolhido[1]}:")
        print(f"\n[1] Nome: {animal_escolhido[1]}")
        print(f"[2] Raça: {animal_escolhido[2]}")
        print(f"[3] Idade: {animal_escolhido[3]}")
        print(f"[4] Estado de saúde: {animal_escolhido[4]}")
        print(f"[5] Comportamento: {animal_escolhido[5]}")
        print(f"[6] Data de chegada: {animal_escolhido[6]}")

        info_quer_editar = int(input("---> Quero editar: "))

        
        if info_quer_editar == 1:
            print(f"\nNome atual: {animal_escolhido[1]}")
            novo_nome = input("Novo nome: ")
            animal_escolhido[1] = novo_nome
        elif info_quer_editar == 2:
            print(f"\nRaça atual: {animal_escolhido[2]}")
            nova_raca = input("Nova raça: ")
            animal_escolhido[2] = nova_raca
        elif info_quer_editar == 3:
            print(f"\nIdade atual: {animal_escolhido[3]}")
            nova_idade = input("Nova idade: ")
            animal_escolhido[3] = nova_idade
        elif info_quer_editar == 4:
            print(f"\nEstado de saúde atual: {animal_escolhido[4]}")
            novo_estado_de_saude = input("Novo estado de saúde: ")
            animal_escolhido[4] = novo_estado_de_saude
        elif info_quer_editar == 5:
            print(f"\nComportamento atual: {animal_escolhido[5]}")
            novo_comportamento = input("Novo comportamento: ")
            animal_escolhido[5] = novo_comportamento
        elif info_quer_editar == 6:
            print(f"\nData de chegada atual: {animal_escolhido[6]}")
            nova_data_de_chegada = input("Nova data de chegada: ")
            animal_escolhido[6] = nova_data_de_chegada

        print("\n[1] Sim\n[2] Não\nVocê deseja editar mais alguma coisa?")
        escolha_quero_editar_mais = int(input("---> 1 ou 2: "))

        if escolha_quero_editar_mais == 1:
            continue
        elif escolha_quero_editar_mais == 2:
            break

def atualizar_animal(escolha):
    if escolha == 3:
        nome_verificacao = input("\nNome do animal: ")

        with open ("data/animais.csv", "r", newline="", encoding="utf-8") as arquivo:
            reader = csv.reader(arquivo)

            animais_nome_verificacao = []

            todas_linhas = []

            for linha in reader:
                todas_linhas.append(linha)

                if nome_verificacao == linha[1]:
                    animais_nome_verificacao.append([linha[0], nome_verificacao,
                                                     linha[2], linha[3], linha[4],
                                                      linha[5], linha[6] ])
                    animal_escolhido = linha
                    
            if len(animais_nome_verificacao) != 1:
                for i in range(len(animais_nome_verificacao)):
                    print(f"[{i+1}] " + " | ".join(animais_nome_verificacao[i]))
                escolha_mesmo_nome = int(input("---> Escolha: "))
                animal_escolhido = animais_nome_verificacao[escolha_mesmo_nome - 1]
                editar_info(animal_escolhido)

            else:
                editar_info(animal_escolhido)  

            with open ("data/animais.csv", "w", newline="", encoding="utf-8") as arquivo:
                writer = csv.writer(arquivo)

                for i in range(len(todas_linhas)):
                    if todas_linhas[i][0] == animal_escolhido[0]:
                        writer.writerow(animal_escolhido)

                    else:
                        writer.writerow(todas_linhas[i])
