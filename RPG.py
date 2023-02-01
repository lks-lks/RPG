print("Olá, imagine que você passou um longo dia no trabalho.\n")
print("Chegando em casa, após todas as suas obrigações você se vê cansado o bastante e decide descansar.\n")
print("Sua cabeça gira frenéticamente ao longo de um grande pesadelo.\n")
print("Você acorda então...\n")
print(41*"*")
print(3*"*","No labirinto da sua mente cansada",3*"*")
print(41*"*")

guerreiro = input("Qual o seu nome ? ")
print("\n")

guerreiro = guerreiro.capitalize()

guerreiro_vida_total = int(50)

print("Você se vê olhando para uma caverna.\n")
print("Algo que não faz sentido para você, inconscientemente te diz para entrar.\n")

print(41*"-")
print("\n")

print(f"{guerreiro}"" então pensa e decide o que fazer\n")
print(2*"-\n")
print("O que você faz?\n")
print("\n")

while True:#laço para que as entradas sejam validadas
    print( " Entra na caverna? Digite - 1\n" , "Dá meia volta e simplesmente vai embora. Digite - 2 ")
    print("\n")


    escolha = input("1 ou 2 ?" )

    if escolha.isdigit():
        escolha = int(escolha)
        if escolha == 1:
            print("Você decide entrar na caverna, tudo é mais escuro do que você pensava. \n")
            print("Você não enxerga um palmo em frente ao nariz, pensa em voltar, mas algo te convida para seguir. . .")
            print("\n")                       
            break

        elif escolha == 2:
            print("Você dá meia volta e vai embora. \n")
            print("Mas sua intuição diz gentilemente ' O cara programou tudo isso pra você apertar o 2 e ir embora ? ' ")
            print("\n")
            print(". . .")
            print("\n") 
            print("Você reflete, suspira pausadamente e decide entrar na caverna")
            break
        
        else:
            print("Opção inválida. Por favor, escolha apenas opções listadas.")
    else:
        print("Por favor digite apenas números.")

print(18*"*")
print("\n")
print("*** ' 'Krak' ' ***")
print("\n")
print(18*"*")

print("Você escuta alguns ruídos vindos do que considera o fundo da caverna. \n")
#começa o enredo dentro da caverna
print("\n")
print(41*"*")
print(3*"*"," Capítulo 1 " "Luz no fim do túnel. ",3*"*")
print(41*"*")
print("\n")
print("Você fica com um certo receio após ouvir o barulho.\n""Mas se lembra que tem um isqueiro no bolso.\n")

while True:
    print("Gostaria de acender o seu isqueiro? ")
    print("Acender - 1\nNão acender - 2")

    isqueiro = input()
    if isqueiro.isdigit():
        isqueiro = int(isqueiro)
        if isqueiro == 1:
            print("Você vê o ambiente se iluminar após a pequena chama surgir.")
            break
        elif isqueiro == 2:
            print("Você decide não acender seu isqueiro\n")
            break
        else:
            print("Opção inválida. Por favor, escolha apenas opções listadas.")
    else:
        print("Por favor digite apenas números.")


    
            
            

        









slime = int(2)
bat = int(2)
skeleton = int(3)
trap= int(4)

#while guerreiro_vida_total and  > 0:
