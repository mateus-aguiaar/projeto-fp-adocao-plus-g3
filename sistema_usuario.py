import src.menus as ui
import src.funcoes as fn
import os
os.system("cls")

while True:
    inicio = input("Digite enter para começar ")

    if inicio == "":
        os.system("cls")
        escolha_especie = input(ui.MENU_ESPECIE_ANIMAL)
        
        animais = fn.verificar_especie(escolha_especie)

        if animais != False:
            pergunta_raca = input("\n[1] Sim \n[2] Não \n\nVocê deseja procurar por uma raça específica? ")
            
            animais = fn.verificar_raca(animais, pergunta_raca)

            if animais != False:
                pergunta_idade = input("\n[1] Sim \n[2] Não \n\nVocê tem preferência de idade do animal? ")

                animais = fn.verificar_idade(animais, pergunta_idade)

                if animais != False:
                    pergunta_comportamento = input(ui.MENU_ESCOLHA_COMPORTAMENTO)

                    fn.verificar_comportamento(animais, pergunta_comportamento)
                    break

                else:
                    break

            else:
                break
            
        else:
            break
    
    else:
        os.system("cls")
