import src.menus as ui
from datetime import datetime, date
import os 
import random

def cadastro_animal(escolha):
    if escolha == 1:      
        nome_animal = input("\nDigite o nome do animal: ").capitalize()
        especie_animal = input("\nDigite a especie do animal: ").lower()
        raca_animal = input("\nDigite a raça do animal: ").lower()
        idade_animal = int(input("\nDigite a idade do animal: "))
        estado_saude_animal = input("\nInforme o estado de saúde do animal: ").capitalize()
        opcao = (input(ui.MENU_COMPORTAMENTO))

        if opcao == "1":
            comportamento_animal = "Agitado"
        elif opcao == "2":
            comportamento_animal = "Calmo"
        elif opcao == "3":
            comportamento_animal = "Neutro"
        elif opcao == "4":
            comportamento_animal = "Medroso"
        
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
            with open ("data/animais.csv", "a", encoding = "utf-8") as arquivo:
                if not arquivo_existe:
                    arquivo.write("id_animal,nome,especie,raca,idade,estado_saude,comportamento,data_chegada\n")
                arquivo.write(f"{id_animal},{nome_animal},{especie_animal},{raca_animal},{idade_animal},{estado_saude_animal},{comportamento_animal},{data_chegada}\n")
                print("\n\033[1;32mCadastro realizado com sucesso!\033[m")
        
        except ValueError:
            print("\033[1;31mValor inválido\033[m")

        return

def verificar_animal(escolha):
    if escolha == 2:
        os.system("cls")
        try:
            with open("data/animais.csv", "r", encoding = "utf-8") as arquivo:
                linhas = arquivo.readlines()
                
                nome_verificacao = input("\nQual o nome do animal: ").lower().capitalize()
                os.system("cls")
                animais_encontrados = []

                for linha in linhas:
                    if not linha.strip() or "id_animal" in linha:
                        continue
                    dados = linha.strip().split(",")
                    if nome_verificacao == dados[1]:
                        animais_encontrados.append(dados)

                while True:
                    if len(animais_encontrados) == 0:
                            print("Nenhum animal foi encontrado!")
                            break

                    elif len(animais_encontrados) == 1:
                            dados = animais_encontrados[0]
                            animal_selecionado = dados
                            print("-" * 50)
                            print(f"{'Nome':<20} {dados[1]}")
                            print(f"{'Raça':<20} {dados[3]}")
                            print(f"{'Idade':<20} {dados[4]} anos")
                            print(f"{'Estado de saúde':<20} {dados[5]}")
                            print(f"{'Comportamento':<20} {dados[6]}")
                            ano,mes,dia = animal_selecionado[7].split("-")
                            print(f"{'Data de chegada':<20} {dia}/{mes}/{ano}")
                        
                    else:
                        print("\nMais de um animal com o mesmo nome:\n")
                        for i, dados in enumerate(animais_encontrados):
                            print(f"[{i+1}] Nome: {dados[1]} | Espécie: {dados[2]} | Raça: {dados[3]} | Comportamento: {dados[6]}")

                        try:
                            selecao_animal = int(input(ui.MENU_ESCOLHA_ANIMAL))
                            if selecao_animal < 1 or selecao_animal > len(animais_encontrados):
                                print("\nOpção inválida")   
                                continue
                            else:   
                                dados = animais_encontrados[selecao_animal - 1] 
                                animal_selecionado = dados
                                os.system("cls")
                                print("-" * 30)
                                print(f"{'Nome':<20} {dados[1]}")
                                print(f"{'Raça':<20} {dados[3]}")
                                print(f"{'Idade':<20} {dados[4]} anos")
                                print(f"{'Estado de saúde':<20} {dados[5]}")
                                print(f"{'Comportamento':<20} {dados[6]}")
                                ano,mes,dia = animal_selecionado[7].split("-")
                                print(f"{'Data de chegada':<20} {dia}/{mes}/{ano}")

                        except ValueError:
                            print("\nDigite um número válido.")
                    
                    funcionarios = ["Mateus Davi","Lucas Calixto","João Vitor","Maria Giulia", "Jullya Medeiros"]
                    gerenciar_animal = int(input(ui.MENU_GERENCIAR_ANIMAL))

                    if gerenciar_animal == 1:
                        if not os.path.exists("data/agendamentos.csv"):
                            with open("data/agendamentos.csv", "w", encoding="utf-8") as arquivo:
                                arquivo.write("id_animal,nome_animal,tarefa,data,responsavel\n")
                        try:
                            with open("data/agendamentos.csv", "r", encoding = "utf-8") as arquivo:
                                agendamentos = arquivo.readlines()
                                
                                agendamentos_encontrados = []
                                
                                for agendamento in agendamentos[1:]:
                                    if not agendamento.strip():
                                        continue
                                    dados_ag = agendamento.strip().split(",")
                                    if dados_ag[0] == animal_selecionado[0]:
                                        agendamentos_encontrados.append(dados_ag)
                                            
                                if agendamentos_encontrados:
                                    os.system("cls")
                                    for ag in agendamentos_encontrados:
                                        print(f"\nTarefa: {ag[2]} | Data: {ag[3]} | Responsável: {ag[4]}")
                                    print("-" * 40)
                                    print(f"{'Nome':<20} {animal_selecionado[1]}")
                                    print(f"{'Raça':<20} {animal_selecionado[3]}")
                                    print(f"{'Idade':<20} {animal_selecionado[4]} anos")
                                    print(f"{'Estado de saúde':<20} {animal_selecionado[5]}")
                                    print(f"{'Comportamento':<20} {animal_selecionado[6]}")
                                    ano,mes,dia = animal_selecionado[7].split("-")
                                    print(f"{'Data de chegada':<20} {dia}/{mes}/{ano}")
                                    break   
                                else:
                                    os.system("cls")
                                    print("Nenhum agendamento foi encontrado.")
                        except ValueError as e:
                                print(f"ERRO2: {e}")
                                print("Digite um valor válido.")      
                        except StopIteration:
                            pass
                        except ValueError:
                            print("Digite um valor válido.")

                    elif gerenciar_animal == 2:
                        animal_tarefa = animal_selecionado[1]
                        id_tarefa = animal_selecionado[0]
                        os.system("cls")
                        menu_tarefa = int(input(ui.MENU_OPCOES_AGENDAMENTOS))
                        if menu_tarefa == 1:
                            tarefa = "Vacina"

                        elif menu_tarefa == 2:
                            tarefa = "Banho"

                        elif menu_tarefa == 3:
                            tarefa = "Consulta veterinária"

                        elif menu_tarefa == 4:
                            tarefa = "Treino"
                        while True:
                            data_verificacao = input("\nQual data você deseja, dia/mês/ano: ")
                            data_tarefa = data_verificacao.replace("/","")
                            if data_tarefa.isdigit() and len(data_tarefa) == 8:
                                data_final = data_tarefa[0:2] + "/"+ data_tarefa[2:4] + "/" + data_tarefa[4:8]
                                break

                            else:
                                print("\nA data deve seguir o padrão dia/mês/ano (XX/XX/XXXX): ")

                        sorteado = random.choice(funcionarios)
                        responsavel_tarefa = sorteado
                        print(f"\nO funcionário responsável pela tarefa é {responsavel_tarefa}.")
                        
                        with open("data/agendamentos.csv", "a", encoding = "utf-8") as arquivo:
                            arquivo.write(f"{id_tarefa},{animal_tarefa},{tarefa},{data_final},{responsavel_tarefa}\n")
                            break
                    else:
                        os.system("cls")
                        break

        except FileNotFoundError:
            os.system("cls")
            print("\n\033[1;31mNenhum animal cadastrado\033[m")

def editar_info(animal_escolhido):
    while True:
        print(f"\nInformações de {animal_escolhido[1]}:")
        print(f"\n[1] Nome: {animal_escolhido[1]}")
        print(f"[2] Espécie: {animal_escolhido[2]}")
        print(f"[3] Raça: {animal_escolhido[3]}")
        print(f"[4] Idade: {animal_escolhido[4]}")
        print(f"[5] Estado de saúde: {animal_escolhido[5]}")
        print(f"[6] Comportamento: {animal_escolhido[6]}")
        print(f"[7] Data de chegada: {animal_escolhido[7]}")

        info_quer_editar = int(input("---> Quero editar: "))

        
        if info_quer_editar == 1:
            print(f"\nNome atual: {animal_escolhido[1]}")
            novo_nome = input("Novo nome: ")
            animal_escolhido[1] = novo_nome
        elif info_quer_editar == 2:
            print(f"\nEspécie atual: {animal_escolhido[2]}")
            nova_especie = input("Nova espécie: ")
            animal_escolhido[2] = nova_especie
        elif info_quer_editar == 3:
            print(f"\nRaça atual: {animal_escolhido[3]}")
            nova_raca = input("Nova raça: ")
            animal_escolhido[3] = nova_raca
        elif info_quer_editar == 4:
            print(f"\nIdade atual: {animal_escolhido[4]}")
            nova_idade = input("Nova idade: ")
            animal_escolhido[4] = nova_idade
        elif info_quer_editar == 5:
            print(f"\nEstado de saúde atual: {animal_escolhido[5]}")
            novo_estado_de_saude = input("Novo estado de saúde: ")
            animal_escolhido[5] = novo_estado_de_saude
        elif info_quer_editar == 6:
            print(f"\nComportamento atual: {animal_escolhido[6]}")
            novo_comportamento = input("Novo comportamento: ")
            animal_escolhido[6] = novo_comportamento
        elif info_quer_editar == 7:
            print(f"\nData de chegada atual: {animal_escolhido[7]}")
            nova_data_de_chegada = input("Nova data de chegada: ")
            animal_escolhido[7] = nova_data_de_chegada

        print("\n[1] Sim\n[2] Não\nVocê deseja editar mais alguma coisa?")
        escolha_quero_editar_mais = int(input("---> 1 ou 2: "))

        if escolha_quero_editar_mais == 1:
            continue
        elif escolha_quero_editar_mais == 2:
            break

def atualizar_animal(escolha):
    if escolha == 3:
        nome_verificacao = input("\nNome do animal: ").capitalize()

        with open ("data/animais.csv", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

            animais_nome_verificacao = []
            todas_linhas = []

            for linha in linhas:
                todas_linhas.append(linha)
                if not linha.strip() or "id_animal" in linha:
                    continue
                dados = linha.strip().split(",")
                if nome_verificacao == dados[1]:
                    animais_nome_verificacao.append(dados)
                    animal_escolhido = dados
                    
            if len(animais_nome_verificacao) == 0:
                print("\nAnimal não encontrado!")
                return

            if len(animais_nome_verificacao) != 1:
                for i in range(len(animais_nome_verificacao)):
                    print(f"[{i+1}] " + " | ".join(animais_nome_verificacao[i]))
                escolha_mesmo_nome = int(input("---> Escolha: "))
                animal_escolhido = animais_nome_verificacao[escolha_mesmo_nome - 1]
                editar_info(animal_escolhido)

            else:
                editar_info(animal_escolhido)  

            with open ("data/animais.csv", "w", encoding="utf-8") as arquivo:
                for i in range(len(todas_linhas)):
                    linha = todas_linhas[i]
                    if not linha.strip() or "id_animal" in linha:
                        arquivo.write(linha)
                        continue
                    dados = linha.strip().split(",")
                    if dados[0] == animal_escolhido[0]:
                        arquivo.write(",".join(map(str, animal_escolhido)) + "\n")
                    else:
                        arquivo.write(linha)

def escolha_especie_animal(escolha):
    
    if escolha == "1":
        especie = "cachorro"
    elif escolha == "2":
        especie = "gato"
    elif escolha == "3":
        especie = "pássaro"
    elif escolha == "4":
        especie = "reptil"
    
    return especie

def verificar_especie(escolha):
    
    especie = escolha_especie_animal(escolha)
    especies_encontradas = []

    with open("data/animais.csv", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            if not linha.strip() or "id_animal" in linha:
                continue
            dados = linha.strip().split(",")
            if dados[2] == especie and dados[5] != "mal":
                especies_encontradas.append(dados)

    if len(especies_encontradas) == 0:
        print("\nInfelizmente não temos nenhum animal dessa especie no momento!")
        
        return False
    
    else:
        os.system("cls")
        return especies_encontradas

def verificar_raca(animais, pergunta):
    os.system("cls")

    if pergunta == "1":
        cont = 1

        for animal in animais:
            print(f"[{cont}] ", animal[3])
            cont += 1
        
        raca = input("\nDigite a raça do animal desejada (digite N para nenhuma): ").strip().lower()

        if raca != "n":
            racas_encontradas = []

            for animal in animais:
                if animal[3] == raca:
                    racas_encontradas.append(animal)
        
            return racas_encontradas

        else:
            print("\nInfelizmente não temos mais raças disponíveis no momento!")
            return False
    else:
        return animais

def verificar_idade(animais, pergunta):
    os.system("cls")

    if pergunta == "1":
        idade_min = int(input("\nDigite a idade mínima do animal (digite -1 para sem idade mínima): "))
        idade_max = int(input("\nDigite a idade máxima do animal (digite -1 para sem idade máxima): "))

        if idade_min == -1 and idade_max == -1:
            os.system("cls")
            return animais
        
        elif idade_min == -1:
            idades_encontradas = []

            for animal in animais:
                if int(animal[4]) <= idade_max:
                    idades_encontradas.append(animal)

            if len(idades_encontradas) == 0:
                print("\nInfelizmente não temos nenhum animal nessa faixa de idade no momento!")
                return False
            
            else:
                os.system("cls")
                return idades_encontradas

        elif idade_max == -1:
            idades_encontradas = []

            for animal in animais:
                if int(animal[4]) >= idade_min:
                    idades_encontradas.append(animal)

            if len(idades_encontradas) == 0:
                print("\nInfelizmente não temos nenhum animal nessa faixa de idade no momento!")
                return False

            else:
                os.system("cls")
                return idades_encontradas

        else:
            idades_encontradas = []

            for animal in animais:
                if int(animal[4]) >= idade_min and int(animal[4]) <= idade_max:
                    idades_encontradas.append(animal)

            if len(idades_encontradas) == 0:
                print("\nInfelizmente não temos nenhum animal nessa faixa de idade no momento!")
                return False

            else:
                os.system("cls")
                return idades_encontradas

    else:
        return animais

def verificar_comportamento(animais, pergunta):
    os.system("cls")

    if pergunta == "1":
        animais_encontrados = []
        
        for animal in animais:
            if animal[6].lower() == "agitado":
                animais_encontrados.append(animal)

        if len(animais_encontrados) == 0:
            print("\nInfelizmente não temos nenhum animal com essas características no momento!")
            return False

        elif len(animais_encontrados) == 1:
            print("\nEncontramos um animal que combina com as características informadas!")
            print(f"\n\tNome: {animais_encontrados[0][1]} \t\tID:{animais_encontrados[0][0]}")                    
            return animais_encontrados
        
        else:
            print("\nEncontramos animais que combinam com as características informadas!")

            for animal in animais_encontrados:
                print(f"\n\tNome: {animal[1]} \t\tID:{animal[0]}")

            return animais_encontrados
    
    elif pergunta == "2":
        animais_encontrados = []
        
        for animal in animais:
            if animal[6].lower() == "calmo":
                animais_encontrados.append(animal)

        if len(animais_encontrados) == 0:
            print("\nInfelizmente não temos nenhum animal com essas características no momento!")
            return False

        elif len(animais_encontrados) == 1:
            print("\nEncontramos um animal que combina com as características informadas!")
            print(f"\n\tNome: {animais_encontrados[0][1]} \t\tID:{animais_encontrados[0][0]}")                    
            return animais_encontrados
        
        else:
            print("\nEncontramos animais que combinam com as características informadas!")

            for animal in animais_encontrados:
                print(f"\n\tNome: {animal[1]} \t\tID:{animal[0]}")

            return animais_encontrados
    
    elif pergunta == "3":
        animais_encontrados = []
        
        for animal in animais:
            if animal[6].lower() == "neutro":
                animais_encontrados.append(animal)

        if len(animais_encontrados) == 0:
            print("\nInfelizmente não temos nenhum animal com essas características no momento!")
            return False

        elif len(animais_encontrados) == 1:
            print("\nEncontramos um animal que combina com as características informadas!")
            print(f"\n\tNome: {animais_encontrados[0][1]} \t\tID:{animais_encontrados[0][0]}")                    
            return animais_encontrados
        
        else:
            print("\nEncontramos animais que combinam com as características informadas!")

            for animal in animais_encontrados:
                print(f"\n\tNome: {animal[1]} \t\tID:{animal[0]}")

            return animais_encontrados
    
    else:
        if len(animais) == 0:
            print("\nInfelizmente não temos nenhum animal com essas características no momento!")
            return False

        elif len(animais) == 1:
            print("\nEncontramos um animal que combina com as características informadas!")
            print(f"\n\tNome: {animais[0][1]} \t\tID:{animais[0][0]}")                    
            return animais
        
        else:
            print("\nEncontramos animais que combinam com as características informadas!")

            for animal in animais:
                print(f"\n\tNome: {animal[1]} \t\tID:{animal[0]}")

            return animais

def deletar_animal(escolha):
    if escolha == 4:
        try:
            nome_verificacao = input("\nNome do animal: ").title()

            with open("data/animais.csv", "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()
            
            animais_nome_verificacao = []

            for linha in linhas:
                if not linha.strip() or "id_animal" in linha:
                    continue
                dados = linha.strip().split(",")
                if nome_verificacao == dados[1].title():
                    animais_nome_verificacao.append(dados)

            if len(animais_nome_verificacao) == 0:
                print("\nAnimal não encontrado!")
                return

            if len(animais_nome_verificacao) == 1:
                animal_escolhido = animais_nome_verificacao[0]
            else:
                for i, animal in enumerate(animais_nome_verificacao, start=1):
                    print(f"[{i}] " + " | ".join(animal))

                escolha_mesmo_nome = int(input("---> Escolha: "))
                animal_escolhido = animais_nome_verificacao[escolha_mesmo_nome - 1]

            print(f"\nInformações de {animal_escolhido[1]}:")
            print(f"\n[1] Nome: {animal_escolhido[1]}")
            print(f"[2] Espécie: {animal_escolhido[2]}")
            print(f"[3] Raça: {animal_escolhido[3]}")
            print(f"[4] Idade: {animal_escolhido[4]}")
            print(f"[5] Estado de saúde: {animal_escolhido[5]}")
            print(f"[6] Comportamento: {animal_escolhido[6]}")
            print(f"[7] Data de chegada: {animal_escolhido[7]}")

            confirmar = int(input("\n[1] Sim \n[2] Não\nTem certeza que deseja deletar este animal? "))

            if confirmar == 1:
                with open("data/animais.csv", "w", encoding="utf-8") as arquivo:
                    arquivo.write("id_animal,nome,especie,raca,idade,estado_saude,comportamento,data_chegada\n")
                    for linha in linhas:
                        if not linha.strip() or "id_animal" in linha:
                            continue
                        dados = linha.strip().split(",")
                        if dados[0] == animal_escolhido[0]:
                            continue
                        arquivo.write(linha)

                print("\n\033[1;32mAnimal deletado com sucesso!\033[m")

            elif confirmar == 2:
                print("\nDeleção cancelada.")

        except FileNotFoundError:
            print("\033[1;31mNenhum animal cadastrado\033[m")