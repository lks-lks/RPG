import time # Primeira modificação introdução  
import random

intro = ["\n",
"Imagine que você passou um longo dia no trabalho.\n",
"Chegando em casa, após todas as suas obrigações você se vê cansado o bastante e decide descansar.\n",
"Sua cabeça gira frenéticamente ao longo de um grande pesadelo.\n",
"Você acorda então...\n"]

for intro in intro:
   print(intro)
   time.sleep(2)

print(41*"*")
print(3*"*","No labirinto da sua mente cansada",3*"*")
print(41*"*")
print("\n") ### fim introdução

guerreiro = input("Qual o seu nome ? ")
print("\n")

guerreiro = guerreiro.capitalize()

guerreiro_vida_total = int(50)

intro_caverna=["Você se vê olhando para uma caverna.\n",
"Algo que não faz sentido para você, inconscientemente te diz para entrar.\n",
"{} então pensa e decide o que fazer\n".format(guerreiro),
"O que você faz?\n"]

for caverna in intro_caverna:
   print(caverna)
   time.sleep(2)


#função escolha 1 caverna
def escolha_1():
  while True:#laço para que as entradas sejam validadas
    print( " Entra na caverna? Digite - 1\n" , "Dá meia volta e simplesmente vai embora. Digite - 2 ")
    print("\n")

    escolha = input("1 ou 2 ? " )

    if escolha.isdigit():
        escolha = int(escolha)
        if escolha == 1:
            escolha_caverna_1=["",
            "Você decide entrar na caverna, tudo é mais escuro do que você pensava. \n",
            "Você não enxerga um palmo em frente ao nariz, pensa em voltar, mas algo te convida para seguir. . .",]
            for opcao in escolha_caverna_1:
              print(opcao, sep = " ", flush = True)
              time.sleep(2)                      
            break

        elif escolha == 2:
            escolha_caverna_2=["",
            "Você dá meia volta e vai embora. \n",
            "Mas sua intuição diz gentilemente ' O cara programou tudo isso pra você apertar o 2 e ir embora ? ' ",
            "\n",
            "...",
            "\n", 
            "Você reflete, suspira pausadamente e decide entrar na caverna. "]
            for escolha in escolha_caverna_2:
              print(escolha, sep = " ", flush = True)
              time.sleep(0.3)         
            break        
        else:
            print("Opção inválida. Por favor, escolha apenas opções listadas.")
            print("\n") 
    else:
        print("Por favor digite apenas números.")
        print("\n") 

escolha_1()

print("Você escuta alguns ruídos vindos do que considera o fundo da caverna. \n")
#começa o enredo dentro da caverna
print("\n")
print(41*"*")
print(3*"*"," Capítulo 1 " "Luz no fim do túnel. ",3*"*")
print(41*"*")
print("\n")

print("Você fica com um certo receio após ouvir o barulho.\n""Mas se lembra que tem um isqueiro no bolso.\n")

#definindo funções para a escolha 2
dano_do_buraco = 6
guerreiro_vida_total_queda = guerreiro_vida_total - dano_do_buraco

def nao_acendeu():
    print("Como você não acendeu o isqueiro não pode ver o grande buraco que estava a sua frente.\n")
    print("Você enfia uma das pernas no buraco e acaba virando o pé.\n")
    print("Com a dor {} solta um grito que ecoa em toda a caverna.".format(guerreiro))
    print("Enquanto sente uma grande dor, você lembra do seu isqueiro e decide usar, porém com o impacto ele caiu de seu bolso.\n")
    print("Frustrado, debilitado e com raiva você tem mais uma surpresa. . .\n")
    print("{} possui agora {} pontos de vida.\n".format(guerreiro,guerreiro_vida_total_queda))
    print("Pontos de vida? Você se questiona. Melhor ter mais cuidado daqui pra frente.")
    
    

def acendeu():
    print("Como você havia acendido o seu isqueiro, pode ver o grande buraco que estava logo a frente.\n")
    print("Você contorna o buraco com muito cuidado.\n")
    print("{} Pensa como é esperto em ter usado a pequena fonte de luz.\n".format(guerreiro))

########

while True:
    print("Gostaria de acender o seu isqueiro? ")
    print("Acender - 1\nNão acender - 2")

    isqueiro = input()
    if isqueiro.isdigit():
        isqueiro = int(isqueiro)
        if isqueiro == 1:
            print("Você vê o ambiente se iluminar após a pequena chama surgir.")
            print("Enquanto ainda escuta barulhos, você decide ir mais a fundo pois sua curiosidade fala mais forte.\n")
            print("Nada faz sentido, você segue tateando as paredes tentando se orientar.\n")
            acendeu()
            break
        elif isqueiro == 2:
            print("Você decide não acender seu isqueiro\n")
            print("Enquanto ainda escuta barulhos, você decide ir mais a fundo pois sua curiosidade fala mais forte.\n")
            print("Nada faz sentido, você segue tateando as paredes tentando se orientar.\n")
            
            nao_acendeu()
            break
        else:
            print("Opção inválida. Por favor, escolha apenas opções listadas.")
    else:
        print("Por favor digite apenas números.")


print("Após a surpresa, seguindo mais a frente você percebe que o barulho havia desaparecido.\n ")
print(" Ao longe na escuridão algo brilha, você sente um frio percorrer sua espinha, mas percebe que não tem outra opção a não ser seguir em frente. . .")

#batalha e saída da caverna

print("\n")
print(39*"*")
print(3*"*"," Capítulo 2 " "Coragem ou medo ?. ",3*"*")
print(39*"*")
print("\n")

print("Avançando você percebe que o ambiente está ficando mais iluminado, tudo indica que é a saída.\n")
print(f"{guerreiro} se alegra ao ver a saída, mas algo ainda não está correto. \n")
print("Uma forma estranha está parada no caminho, o brilho que você havia visto anteriormente, são seus olhos. . . ")
print("Você precisa enfrentar a criatura para sair.")

goblin = 10
inimigo = goblin

#definindo a função de batalha

def batalha(inimigo,guerreiro_vida_total):
  while inimigo > 0 and guerreiro_vida_total > 0:
    print("Deseja atacar - 1 \nCorrer - 2 ")
    entrada = input("1 ou 2 ? ")
    if entrada.isdigit():
      entrada =int(entrada)
      if entrada == 1:#laço de ataque
        print("Você ataca sem piedade!")
        hit = 1
        inimigo -= hit
        print(f"Você acertou com {hit} de dano! Agora o inimigo tem {inimigo} de vida. ")
        if inimigo == 0:
          print("Você venceu")#fim do laço de ataque        
      elif entrada == 2:
        print("Você tenta correr, mas não tem sucesso!")
        hit =1
        guerreiro_vida_total -=hit      
        print(f"Na sua tentativa frustrada de fuga o inimigo te acerta com {hit} de dano!\n")
        print(f"Agora você tem {guerreiro_vida_total} de vida.")
        if guerreiro_vida_total == 0:
          print("Sua aventura termina aqui!\n""Você acorda em sua cama pensando...\n")
          print("Eu preciso chamar esse rapaz para uma entrevista! ") 
      else:
            print("Opção inválida. Por favor, escolha apenas opções listadas.")
    else:
        print("Por favor digite apenas números.")

########            
            
#while true:
  # print("Você precisa lutar para sair.\n""Mas com sua afobação, {} precisa pensar no que fazer)
        









slime = int(2)
bat = int(2)
skeleton = int(3)
trap= int(4)

#while guerreiro_vida_total and  > 0:
