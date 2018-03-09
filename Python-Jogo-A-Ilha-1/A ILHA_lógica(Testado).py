
#Váriável de tempo
import time
"""

-------------------------THE ISLAND-------------------


-------------------------
BY. DAVID, GREGORY E GOIS

"""

#Logo do game
print("\n\n         \033[01;30;46m THE ISLAND \033[m   \n\n")

#INICIO
inicio = str.upper(input('Digite \033[01;36minicio\033[m para começar:'))
time.sleep(1)

#LOOP
while inicio != 'INICIO':
    print('Você \033[01;31mNAO\033[m sabe nem escrever "inicio" como vai começar o jogo assim? tente novamente :)')
    inicio = str.upper(input('\nDigite \033[01;31minicio\033[m para começar:'))

#INTRO
print("\n\033[1mParabéns\033[m, você foi convidado (a) a uma incrível viagem para um lindo resort. \n"
      "Imediatamente você arruma suas malas e se prepara para a viagem\n")

#DADOS DO JOGADOR
nome = str.upper(input("Digite seu nome: \n"))
time.sleep(1)

#A VIAGEM
print('\n\n', nome,
", você entra no avião e vai para seu assento, mesmo se sentindo desconfortável você acaba pegando no sono...\n ZzZzZ...ZzZzZ...ZzZzZ...\n")
print("Parece que você está dormindo....")
time.sleep(3)
print("\n\nVocê acorda em meio a uma terrível turbulência, olha para os lados e vê malas caindo...\n")
time.sleep(3)
print("Gritos e choro ...")
time.sleep(3)
print("\nPassageiros \033[02;36mATERRORIZADOS\033[m...\n")
time.sleep(3)
print("Você percebe que a situação é grave...\n\n OOOOOHH!!!! O AVIÃO ESTÁ CAINDO!!!\033[01;3BOOOOW!!!\033[m... \n"
      "CA...IND...DOOOOOOOOO\n\n Você fecha os olhos e não vê mais nada...")
time.sleep(3)


#AFOGAMENTO
input('\n\nVocê sente o sol em seu rosto e um leve gosto de sal na boca...')


#A ILHA
print("\n\n\nVocê acorda desorientado em uma praia... \n\n\n\n\n")
time.sleep(3)


#REGRAS
print("                        Bem vindo a \033[01;30;46m ILHA \033[m \n\n")
print("Suas escolhas a partir de agora vai decidir se você conseguirá sobreviver a essa situação,")
time.sleep(3)
print("escolha as alternativas com sabedoria, você tem uma pontuação de vida “100”\,")
time.sleep(3)
print("escolhas erradas farão você perder pontos de vida escolhas certas podem aumentar ou não mudar seus pontos de vida,")
time.sleep(3)
print("tente achar um meio de sobreviver e ser resgatado.\n\n\n\n")
time.sleep(3)



# VARIAVEIS
import random

hp = int(100)
action = int(0)

# -----------------------------------------------------------------------------------------------------------------------------------------------------
while action <= 5:

    # PRIMEIRA DESISÂO
    input("Você acorda e existe uma floresta à sua frente, mas está escurecendo, "
          "não deve ter mais que 1h do luz, você está faminto e muito cansado."
          "\npressione (ENTER) para continuar... ")
    Decisao1 = str.upper(input("Qual ação você quer tomar ?\n"
                               "A - Procurar comidas em arvores próximas a costa.\n"
                               "B - Dormir a beira da praia e esperar o próximo dia para procurar comida.\n"
                               "C - Tentar pegar algum peixe com a mão.\n\nDigite a letra correspondente a opção para para continuar:\n\n"))

    while Decisao1 != "A" and Decisao1 != "B" and Decisao1 != "C":
        print("\n Você deve escolher entre as opções A, B ou C. Digite corretamente a opção para continuar.\n")
        Decisao1 = str.upper(input("A - Procurar comidas em arvores próximas a costa.\n"
                                   "B - Dormir a beira da praia e esperar o próximo dia para procurar comida.\n"
                                   "C - Tentar pegar algum peixe com a mão.\n\nDigite a letra correspondente a opção para para continuar:\n\n"))
    # ROLETA
    Conseq1 = random.randint(1, 10)

    # PERGUNTAS
    if hp > 0:

        if Decisao1 == "A":

            if 5 > Conseq1 < 3:
                print("Você achou uma bananeira ! Encheu a pança de banana e pegou no sono. +10 pontos de vida.")
                hp = hp + 10
            else:
                print("Você comeu uma estranha fruta em uma flor desconhecida e morreu envenenado !")
                hp = 0
        if Decisao1 == "B":
            if Conseq1 < 5:
                print("Você teve uma boa noite de sono ao relento. + 5 pontos de vida.")
                hp = hp + 5
            else:
                print("Uma alcateia de lobos te encontrou enquanto você dormia !! Você foi devorado !")
                hp = 0
        if Decisao1 == "C":
            if Conseq1 < 5:
                print("Você conseguiu pegar uma truta e a devorou crua de tanta fome !! + 10 pontos de vida.")
                hp = hp + 10
            else:
                print("Você tentou pegar um peixe com a mão, se cansou e foi se deitar. - 20 pontos de vida.")
                hp = hp - 20
    action = action + 1

    # Fim de Jogo
    if hp <= 0:
        print("GAME OVER!!!")
        break

    # seu hp é igual

    if hp >= 100:
        print("Seu nível é Richard Rasmussen, continue assim! ")
    elif hp < 100 and hp >= 75:
        print("Seu nível é Sobrevivente, Parabéns!!")
    elif hp <= 74 and hp >= 50:
        print("Você é escoteiro, ainda tem muito a aprender")
    elif hp < 50 and hp >= 25:
        print("Você está com pouco hp, cuidado, seu nível é morador de cidade grande")
    elif hp < 25 and hp <= 0:
        print("Cuidado!!! você está quase morrendo, seu nível é igual ao do bozo, "
              "\nnão tem mais da o que fazer?")
    print("Você está com {} pontos "
          "de vida".format(hp))

    # -----------------------------------------------------------------------------------------------------------------------------------------------------


    # SEGUNDA DESISÂO
    input("\n\n O dia amanheceu seu objetivo é encontrar água potável e "
          "comida você entra na floresta avista um coqueiro."
          "\npressione (ENTER) para continuar... \n")
    Decisao2 = str.upper(input("Qual ação você irá tomar ?\n"
                               "A - Escalar o coqueiro e tentar pegar um coco.\n"
                               "B - Jogar um pedaço de madeira para tentar acertar o coco.\n"
                               "C - Ignorar e continuar andando floresta adentro.\n"
                               "\nDigite a letra correspondente a opção para para continuar:\n\n"))
    while Decisao2 != "A" and Decisao2 != "B" and Decisao2 != "C":
        print("\n Você deve escolher entre as opções A, B ou C. Digite corretamente a opção para continuar.\n")
        Decisao2 = str.upper(input("A - Escalar o coqueiro e tentar pegar um coco.\n"
                                   "B - Jogar um pedaço de madeira para tentar acertar o coco.\n"
                                   "C - Ignorar e continuar andando floresta adentro.\n"
                                   "\nDigite a letra correspondente a opção para para continuar:\n\n"))

    # ROLETA
    Conseq2 = random.randint(1, 10)

    # PERGUNTAS
    if Decisao2 == "A":
        if Conseq2 < 5:
            print(
                "Depois de uma tortuosa escalada ao coqueiro, você conseguiu pegar um coco ! Á agua estava fresca e deliciosa ! +20 pontos de vida.")
            hp = hp + 20
        else:
            print(
                "Você não percebeu que havia uma cobra venenosa no topo do coqueiro !! Você foi picado e teve uma morte lenta e dolorosa !")
            hp = 0
    elif Decisao2 == "B":
        if Conseq2 < 5:
            print(
                "Na mosca ! Você acertou um pedaço de madeira em um coqueiro e ele caiu. Á agua estava fresca e deliciosa ! + 20 pontos de vida.")
            hp = hp + 20
        else:
            print("Errou ! Você tentou jogar um pedaço de madeira, mas não acertou o coqueiro. - 5 pontos de vida !")
            hp = hp - 5
    elif Decisao2 == "C":
        if Conseq2 < 5:
            print("Você ignorou o coqueiro e continuou mata a dentro.")
        else:
            print("Você ignorou o coqueiro e continuou mata a dentro..."
                  "\nPorém, se deparou com um tigre faminto !! Você foi devorado !!")
            hp = 0

    action = action + 1

    # Fim de Jogo
    if hp <= 0:
        print("GAME OVER!!!")
        break

    # seu hp é igual

    if hp >= 100:
        print("Seu nível é Richard Rasmussen, continue assim! ")
    elif hp < 100 and hp >= 75:
        print("Seu nível é Sobrevivente, Parabéns!!")
    elif hp <= 74 and hp >= 50:
        print("Você é escoteiro, ainda tem muito a aprender")
    elif hp < 50 and hp >= 25:
        print("Você está com pouco hp, cuidado, seu nível é morador de cidade grande")
    elif hp < 25 and hp <= 0:
        print("Cuidado!!! você está quase morrendo, seu nível é igual ao do bozo, "
              "\nnão tem mais da o que fazer?")
    print("Você está com {} pontos de vida".format(hp))

    # -----------------------------------------------------------------------------------------------------------------------------------------------------


    # TERCEIRA DESISÂO
    input("\n\n 3-	Você volta para a praia e anda pela costa, ao fim você acha uma caverna, e decide entrar,\n"
          " ossos ao verificá-los você percebe que são de algum animal provavelmente de algum porco,"
          "\n com essa informação em mente você entra com muita cautela e procura de algum animal que possa estar dentro da caverna, \n"
          "mas só acha alguns cogumelos, essa procura deixou-lhe muito faminto, o que fazer?"
          "\npressione (ENTER) para continuar... \n")
    Decisao3 = str.upper(input("Qual ação você irá tomar ?\n"
                               "A - Comer eles cru.\n"
                               "B - Fazer uma fogueira, assar eles e comer.\n"
                               "C - Deixar onde estão e ficar com fome.\n"
                               "\nDigite a letra correspondente a opção para para continuar:\n\n"))
    # LOOP
    while Decisao3 != "A" and Decisao3 != "B" and Decisao3 != "C":
        print("\n Você deve escolher entre as opções A, B ou C. Digite corretamente a opção para continuar.\n")
        Decisao3 = str.upper(input("A - Comer eles cru.\n"
                                   "B - Fazer uma fogueira, assar eles e comer.\n"
                                   "C - Deixar onde estão e ficar com fome.\n"
                                   "\nDigite a letra correspondente a opção para para continuar:\n\n"))
    # ROLETA
    Conseq3 = random.randint(1, 10)

    # PERGUNTAS
    if Decisao3 == "A":
        if Conseq3 <= 5:
            print("Você mata sua fome e ganha +20 pontos de vida.")
            hp = hp + 20
        else:
            print("Você está alucinado, sente calor... e começa a tirar a roupa e correr na praia pelado tropeça em "
                  "uma pedra bate a cabeça e morre ! .")
            hp = 0
    if Decisao3 == "B":
        if Conseq3 <= 5:
            print("Eles queimaram e o cheiro do cogumelo queimdo o fez passar mal, você perdeu - 20 de vida")
            hp = hp - 20
        else:
            print("Parabéns, você os assou bem e ganhou +10 pontos de vida !")
            hp = hp + 10
    if Decisao3 == "C":
        if Conseq3 <= 5:
            print("Você ignorou os cogumelos e desmaiou de fome, -30 pontos")
            hp = hp - 30
        else:
            print("Você volta para praia e acha um carangueijo, come e isso te revigora + 20 pontos")
            hp = hp + 20
    action = action + 1

    # Fim de Jogo
    if hp <= 0:
        print("GAME OVER!!!")
        break

    # seu hp é igual

    if hp >= 100:
        print("Seu nível é Richard Rasmussen, continue assim! ")
    elif hp < 100 and hp >= 75:
        print("Seu nível é Sobrevivente, Parabéns!!")
    elif hp <= 74 and hp >= 50:
        print("Você é escoteiro, ainda tem muito a aprender")
    elif hp < 50 and hp >= 25:
        print("Você está com pouco hp, cuidado, seu nível é morador de cidade grande")
    elif hp < 25 and hp <= 0:
        print("Cuidado!!! você está quase morrendo, seu nível é igual ao do bozo, "
              "\nnão tem mais da o que fazer?")

    print("Você está com {} pontos de vida".format(hp))

    # -----------------------------------------------------------------------------------------------------------------------------------------------------

    # QUARTA DESISÂO
    input("\n\n 4-	Depois de algumas semanas você está começando a entender como sobreviver,"
          " e sabe que na ilha não tem muitos alimentos, "
          "\nmas possivelmente porcos, pois ouviu grunidos todas as noites na floresta, "
          "\nvocê tem alguns cocos, mas sabe que se quiser sobreviver vai precisar de mais alimentos"
          "\npressione (ENTER) para continuar... ")
    Decisao4 = str.upper(input("Qual ação você irá tomar ?\n"
                               "A - Ir a procura dos porcos.\n"
                               "B - Tentar achar mais frutas\n"
                               "C - Tentar pegar peixes..\n"
                               "\nDigite a letra correspondente a opção para para continuar:\n\n"))
    # LOOP
    while Decisao4 != "A" and Decisao4 != "B" and Decisao4 != "C":
        print("\n Você deve escolher entre as opções A, B ou C. Digite corretamente a opção para continuar.\n")
        Decisao4 = str.upper(input("A - Ir a procura dos porcos.\n"
                                   "B - Tentar achar mais frutas\n"
                                   "C - Tentar pegar peixes..\n"
                                   "\nDigite a letra correspondente a opção para para continuar:\n\n"))

    # ROLETA
    Conseq4 = random.randint(1, 10)

    # PERGUNTAS
    if Decisao4 == "A":
        if Conseq4 <= 5:
            print("Você corre mas não consegue alcança-los, você fica desorientado e demora horas para "
                  "chegar devolta a praia, cansado e com fome, - 20 de hp")
            hp = hp - 20
        else:
            print("Você encontra uma manada e consegue capiturar um, parabéns, + 30 hp !")
            hp = hp + 30
    if Decisao4 == "B":
        if Conseq4 < 5:
            print("Na mosca ! Você entrou na floresta e encontrou uma arvóre repleta de manga! + 20 pontos de vida.")
            hp = hp + 20
        else:
            print(
                "Vai a floresta e vê um pé de manga, você encontra uma pedra e tenta arremessar, mas acaba acertando um enxame de abelhas. - 50 pontos de vida !")
            hp = hp - 50
    if Decisao4 == "C":
        if Conseq4 < 5:
            print("Show!, você pesca um peixão!, mais 30 de hp")
            hp = hp + 30
        else:
            print(
                "Você faz uma lança e vai para o mar, sente que pisou em algo pontiagudo, não sabe o que é, mas dói muito, sente uma dor muito forte no peito e morrer ali mesmo...")
            hp = 0

    action = action + 1

    # Fim de Jogo
    if hp <= 0:
        print("GAME OVER!!!")
        break

    # seu hp é igual

    if hp >= 100:
        print("Seu nível é Richard Rasmussen, continue assim! ")
    elif hp < 100 and hp >= 75:
        print("Seu nível é Sobrevivente, Parabéns!!")
    elif hp <= 74 and hp >= 50:
        print("Você é escoteiro, ainda tem muito a aprender")
    elif hp < 50 and hp >= 25:
        print("Você está com pouco hp, cuidado, seu nível é morador de cidade grande")
    elif hp < 25 and hp <= 0:
        print("Cuidado!!! você está quase morrendo, seu nível é igual ao do bozo, "
              "\nnão tem mais da o que fazer?")
    print("Você está com {} pontos de vida".format(hp))

    # -----------------------------------------------------------------------------------------------------------------------------------------------------
    # ULTIMA DESISÂO

    input(
        "\n\n Mais um dia chegou, você esta de na costa pensando, já adquiriu ferramentas e experiência na ilha, mas ainda não sabe "
        "o que fazer quando vê um navio ao horizonte..."
        "\npressione (ENTER) para continuar...  ")
    print("repleto de esperança você decide criar um meio para que caso passe outro navio alguém possa te enxergar.\n")
    time.sleep(2)
    Decisao5 = str.upper(input("Qual ação você irá tomar ?\n"
                               "A - Criar um totem com pedaços de arvores caídos.\n"
                               "B - Criar uma jangada para tentar se aproximar do navio.\n"
                               "C - Fazer uma fogueira enorme.\n"
                               "\nDigite a letra correspondente a opção para para continuar:\n\n"))
    # LOOP
    while Decisao5 != "A" and Decisao5 != "B" and Decisao5 != "C":
        print("\n Você deve escolher entre as opções A, B ou C. Digite corretamente a opção para continuar.\n")
        Decisao5 = str.upper(input("A - Criar um totem com pedaços de arvores caídos.\n"
                                   "B - Criar uma jangada para tentar se aproximar do navio.\n"
                                   "C - Fazer uma fogueira enorme.\n"
                                   "\nDigite a letra correspondente a opção para para continuar:\n\n"))

    # ROLETA
    Conseq5 = random.randint(1, 10)

    xp = 1

    # PERGUNTAS
    if Decisao5 == "A":
        if Conseq5 <= 5:
            print("O totem é avistado e o navio sinaliza em sua direção, Parabéns Você foi salvo!!!")
            xp = 1
        else:
            print("Você faz o totem e quando tenta ergue-lo, ele cai na sua cabeça e você morre")
            hp = 0
    if Decisao5 == "B":
        if Conseq5 <= 5:
            print("Você consegue fazer o barco em menos de 30 minutos e o "
                  "navio está perto da costa, eles conseguem te ver e você é salvo!")
            xp = 1
        else:
            print(
                "Você não consegue terminar o barco a tempo e o navio já está fora do seu alcance, ficará preso na ILHA para sempre, hahahaha")
            xp = 0
    if Decisao5 == "C":
        if Conseq5 <= 5:
            print("Sua fogueira é avistada e o navio simboliza que você foi visto, Parabéns Você Foi Salvo!!")
            xp = 1
        else:
            print(
                "Começa a chover e sua fogueira não acende, infelizmente você ficará o resto da vida na ILHA, hahhahaha!")
            xp = 0

    # Fim de Jogo
    if hp <= 0:
        print("GAME OVER!!!")
        break

    # seu hp é igual

    if hp >= 100 and xp == 1:
        print("Seu nível é Richard Rasmussen, zerou o jogo no máximo, Você é épico!!!! ")
    elif hp < 100 and hp >= 75 and xp == 1:
        print("Seu nível é Sobrevivente, Parabéns!!")
    elif hp <= 74 and hp >= 50 and xp == 1:
        print("Você é escoteiro, ainda tem muito a aprender")
    elif hp < 50 and hp >= 25 and xp == 1:
        print("Você escapou por pouco!!!\n"
              "Seu nível é Macaco Velho da Cidade")
    elif hp < 25 and hp <= 0 and xp == 1:
        print("Seu jogo foi na sorte...mesmo assim você sobrevivel, "
              "\nnas próximas vezes que for viajar leve alguém que saiba sobreviver!\n"
              "Seu nível é BOZO")

    action = action + 1
    print("Você TERMINOU com {} pontos de vida".format(hp))

    if action == 5:
        break

"""

    -------------------------Créditos---------------------


    -------------------------------------------------------

    A ilha é um jogo de interação simuntania que interage com
    o interlocutor dando a ela a chance de SOBREVIVER ou MORRER na
                            (THE ISLAND)


    - Mackenzie -
       - Lab. de Programação -
          - Prof. Ilana Concilio -
    FCI - N1
    Gregory Fernandes - TIA - 41706692
    Matheus Gois - TIA - 41746491

    FAU - 413B
    David Couto - TIA - 41382722
"""