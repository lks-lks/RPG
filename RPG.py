import time # Primeira modificação introdução  
import random

intro = ["\n",
"Imagine que você passou um longo dia no trabalho.\n",
"Chegando em casa, após todas as suas obrigações você se vê cansado o bastante e decide descansar.\n",
"Sua cabeça gira frenéticamente ao longo de um grande pesadelo.\n",
"Você acorda então...\n"]

for intro in intro:
   print(intro)
   time.sleep(0.5)

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
   time.sleep(0.5)


#função escolha 1 caverna

escolha_caverna_1=["",
            "Você decide entrar na caverna, tudo é mais escuro do que você pensava. \n",
            "Você não enxerga um palmo em frente ao nariz, pensa em voltar, mas algo te convida para seguir. . .\n",]

escolha_caverna_2=["",
            "Você dá meia volta e vai embora. \n",
            "Mas sua intuição diz gentilemente ' O cara programou tudo isso pra você apertar o 2 e ir embora ? ' ",
            "\n",
            "...",
            "\n", 
            "Você reflete, suspira pausadamente e decide entrar na caverna. \n"]

def escolha_1():
  while True:#laço para que as entradas sejam validadas
    
    print( " Entra na caverna? Digite - 1. \n" , "\n", "Dá meia volta e simplesmente vai embora. Digite - 2. \n")
    escolha = input(" 1 ou 2 ? ")

    if escolha.isdigit():
        escolha = int(escolha)
        if escolha == 1:            
            for opcao in escolha_caverna_1:
              print(opcao, sep = " ", flush = True)
              time.sleep(0.5)                      
            break
        elif escolha == 2:  
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

ruido =["Você escuta alguns ruídos vindos do que considera o fundo da caverna. \n"]
for ruido in ruido:
   print(ruido, sep=" ", flush= True)
   time.sleep(0.5)
#começa o enredo dentro da caverna

print(41*"*")
print(3*"*"," Capítulo 1 " "Luz no fim do túnel. ",3*"*")
print(41*"*")
print("\n")

time.sleep(0.5)

ruido_caverna =["Você fica com um certo receio após ouvir o barulho.\n","Mas se lembra que tem um isqueiro no bolso.\n"]
for ruido in ruido_caverna:
   print(ruido, sep=" ", flush= True)
   time.sleep(1)

#definindo funções para a escolha 2
dano_do_buraco = 6
guerreiro_vida_total_queda = guerreiro_vida_total - dano_do_buraco

nao_acendeu = ["Você decide não acender seu isqueiro\n",
"Enquanto ainda escuta barulhos, você decide ir mais a fundo pois sua curiosidade fala mais forte.\n",
"Nada faz sentido, você segue tateando as paredes tentando se orientar.\n",
"...\n",
"Como você não acendeu o isqueiro não pode ver o grande buraco que estava a sua frente.\n",
"Você enfia uma das pernas no buraco e acaba virando o pé.\n",
"Com a dor {} solta um grito que ecoa em toda a caverna.\n".format(guerreiro),
"Enquanto sente uma grande dor, você lembra do seu isqueiro e decide usá-lo agora, porém com o impacto ele caiu de seu bolso.\n",
"Frustrado, debilitado e com raiva você tem mais uma surpresa. . .\n",
"{} possui agora {} pontos de vida.\n".format(guerreiro,guerreiro_vida_total_queda),
"Pontos de vida? Você se questiona. Melhor ter mais cuidado daqui pra frente.\n"]
    
    

acendeu = ["Você vê o ambiente se iluminar após a pequena chama surgir.\n",
"Enquanto ainda escuta barulhos, você decide ir mais a fundo pois sua curiosidade fala mais forte.\n",
"Nada faz sentido, você segue tateando as paredes tentando se orientar.\n",
"Como você havia acendido o seu isqueiro, pode ver o grande buraco que estava logo a frente.\n",
"Você contorna o buraco com muito cuidado.\n",
"{} pensa ' foi bom ter usado a pequena fonte de luz...'.\n".format(guerreiro)]

########

while True:
    print("Gostaria de acender o seu isqueiro? ")
    print("Não acender - 1.\nAcender - 2. ")

    isqueiro = input()
    if isqueiro.isdigit():
        isqueiro = int(isqueiro)
        if isqueiro == 1:
            for frase in nao_acendeu:
              print(frase, sep= " ", flush= True)
              time.sleep(0.5)
            break
        elif isqueiro == 2:
            for acendeu in acendeu:
              print(acendeu, sep=" ",flush= True)
              time.sleep(0.5)
            break
        else:
            print("Opção inválida. Por favor, escolha apenas opções listadas.\n")
    else:
        print("Por favor digite apenas números.\n")

time.sleep(1)

surpresa = ["Após a surpresa, um pouco mais a frente você nota que o barulho desapareceu.\n ",
"Ao longe na escuridão algo brilha, você sente um frio percorrer sua espinha, mas percebe que não tem outra opção a não ser seguir em frente. . .\n"]
for surpresa in surpresa:
   print(surpresa, sep="", flush=True)
   time.sleep(0.5)

#batalha e saída da caverna

print("\n")
print(39*"*")
print(3*"*"," Capítulo 2 " "Coragem ou medo ?. ",3*"*")
print(39*"*")
print("\n")

continuando_a_surpresa = ["Conforme avança, você percebe que o ambiente está ficando mais iluminado.\n",
"{} se alegra ao ver a saída.\n".format(guerreiro),
"Porém uma forma estranha está parada no caminho, o mesmo brilho que você havia visto anteriormente . . . \n",
"Você deve enfrentar a criatura se quiser sair!!"]

for continuando in continuando_a_surpresa:
   print(continuando,sep="",flush=True)
   time.sleep(0.5)




#definindo a função de batalha


def batalha(inimigo,guerreiro_vida_total):
  while inimigo > 0 and guerreiro_vida_total > 0:
    print("Deseja atacar - 1 \nCorrer - 2 ")
    entrada = input("1 ou 2 ? ")
    if entrada.isdigit():
      entrada =int(entrada)
      if entrada == 1:#laço de ataque
        print("Você ataca sem piedade!")
        hit = random.randint(1,2)
        inimigo -= hit
        print(f"Você acertou com {hit} de dano! Agora o inimigo tem {inimigo} de vida. ")
        if inimigo <= 0:
          print("Você venceu")#fim do laço de ataque 
          break       
      elif entrada == 2:
        print("Você tenta correr, mas não tem sucesso!")
        hit = random.randint(3,10)
        guerreiro_vida_total -=hit      
        print(f"Na sua tentativa frustrada de fuga o inimigo te acerta com {hit} de dano!\n")
        print(f"Agora você tem {guerreiro_vida_total} de vida.\n")
        if guerreiro_vida_total <= 0:
          print("Sua aventura termina aqui!\n""Você acorda em sua cama pensando...\n")
          print("Eu preciso chamar esse rapaz para uma entrevista! ")
          
          break 
      else:
            print("Opção inválida. Por favor, escolha apenas opções listadas.")
    else:
        print("Por favor digite apenas números.")


n_isqueiro=["Com a penalidade da queda no buraco, {} começa a batalha com {} pontos de vida.\n".format(guerreiro,guerreiro_vida_total_queda),
"A criatura avança, e você pecebe que é um goblin asqueiroso.\n",
"Mesmo debilitado, você decide lutar!!"]

s_isqueiro= [" Você atira seu isqueiro em direção a criatura !\n",
"A criatura avança, e você pecebe que é um goblin asqueiroso.\n",
"Com medo, mas cheio de energia você decide lutar!!\n"]


#definindo o laço do isqueiro

while True:
    print("Você ainda possui o seu isqueiro? ")
    print("Não - 1.\nSim - 2. ")
    goblin = random.randint(1,6)

    resposta = input()
    if resposta.isdigit():
        resposta = int(resposta)
        if resposta == 1:
            for frase in n_isqueiro:
              print(frase, sep= " ", flush= True)
              time.sleep(0.5)
            batalha(goblin,guerreiro_vida_total_queda)
            quit(True)
            
            break
        elif resposta == 2:
            for acendeu in s_isqueiro:
              print(acendeu, sep=" ",flush= True)
              time.sleep(0.5)
            batalha(goblin,guerreiro_vida_total_queda)
            quit(True)
            
            break
        else:
            print("Opção inválida. Por favor, escolha apenas opções listadas.\n")
    else:
        print("Por favor digite apenas números.\n")

#continuar 
