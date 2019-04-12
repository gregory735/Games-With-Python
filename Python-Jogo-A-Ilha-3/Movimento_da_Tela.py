"""
Jogo feito pelos alunos da Universidade Presbiteriana Mackenzie, da Faculdade de Computação e Informática
Feito para a diciplina de ALGORITMOS E PROGRAMACAO II, como poposta de projeto final
Alunos: Grégory Fernandes(41706692) e Matheus Gois(41746491)

Jogo desenvolvido em maio de 2018.
"""



import pygame, random,time
from pygame.locals import *

pygame.init()

# ---------------------------------------------Tamanho da tela-----------------------------------------------------------
comprimento_ecra = 640
altura_ecra = 480
ecra = pygame.display.set_mode((comprimento_ecra, altura_ecra))
pygame.display.set_caption('A Ilha 3')
vivo = True
verificador = False
global pontuacao1, pontuacao_final
potuacao1 = 0
pontuacao_final = 0


def creditos():
    while True:
        branco = (255, 255, 255)
        botao_retornar_jogo = pygame.image.load('IMG/botao_retornar_jogo.png')
        logo = pygame.image.load('IMG/logo.png')
        ecra.blit(logo, (230, 30))
        fonte = pygame.font.Font(None, 30)
        creditos1 = fonte.render('Feito por: Gois',3, branco)
        creditos2 = fonte.render('Feito por: Greg',3, branco)
        creditos3 = fonte.render('Musica por DJLuk',3, branco)
        ecra.blit(creditos1, (260, 220))
        ecra.blit(creditos2, (260, 250))
        ecra.blit(creditos3, (250, 420))

        pygame.display.flip()
        time.sleep(5)
        break

creditos()

def inst():
    while True:
        t = pygame.image.load('IMG/Inst.png')
        ecra.blit(t, (0, 0))
        pygame.display.flip()
        time.sleep(3)
        break

def morte():
    global vivo,pontuacao_final
    pygame.mixer.music.stop()
    morte = True
    posicao_do_select = 270
    vida = 3
    branco = (255, 255, 255)
    while morte:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.flip()

        tecla_pressionada = pygame.key.get_pressed()

        if tecla_pressionada[K_BACKSPACE]:
            pygame.quit()

        if  posicao_do_select == 270 and tecla_pressionada[K_SPACE]:
            vivo = True
            break

        if  posicao_do_select == 335 and tecla_pressionada[K_SPACE]:
            break

        pygame.display.flip()
        bg = pygame.image.load('IMG/bg.png')
        logo = pygame.image.load('IMG/logo.png')

        botao_retornar_jogo = pygame.image.load('IMG/botao_retornar_jogo.png')
        selecionar_botao = pygame.image.load('IMG/select.png')

        ecra.blit(bg, (0, 0))
        ecra.blit(botao_retornar_jogo, (180, 260))
        ecra.blit(logo, (230, 30))
        fonte = pygame.font.Font(None, 30)
        pontuacao = fonte.render('Pontuação máxima: ' + str(pontuacao_final), 2, branco)
        sorte = fonte.render('Boa sorte na próxima!', 2, branco)
        ecra.blit(pontuacao, [210, 350])
        ecra.blit(sorte, [220, 400])
        ecra.blit(selecionar_botao, (120, posicao_do_select))
        pygame.display.flip()




def musica():
    pygame.mixer.music.load("Som/som.wav")
    pygame.mixer.music.play()


def somDaMorte():
    pygame.mixer.music.load("Som/lose.ogg")
    pygame.mixer.music.play()
    time.sleep(0.6)


def jogo():
    global vivo, pontuacao_final,potuacao1
    # ------------------------------------------- Cores ---------------------------------------------------------------------
    vermelho = (255, 0, 0)
    azul = (0, 0, 255)
    preto = (0, 0, 0)
    verde = (0, 255, 0)
    branco = (255,255,255)
    # -------------------------------------------- circulo ------------------------------------------------------------------
    raio_circulo = 10

    # ------------------------------------------ Velocidade vida e posições -------------------------------------------------
    xpos = 320
    ypos = 240
    movimento_em_x = 2
    movimento_em_y = 2
    velocidade_do_asteroide = 2
    relogio = pygame.time.Clock()
    fps = 90
    vida = 3
    imgvida = pygame.image.load('IMG/vida.png')

    # --------------------------------------- asteroides que descem (down) --------------------------------------------------
    posicao_dos_asteroides_em_x = random.randint(10, 208)
    posicao_dos_asteroides_em_x2 = random.randint(228, 416)
    posicao_dos_asteroides_em_x3 = random.randint(436, 630)
    posicao_dos_asteroides_em_y_down = -20
    posicao_dos_asteroides_em_y_down2 = -20
    posicao_dos_asteroides_em_y_down3 = -20

    # ---------------------------------------- asteroides que sobem (Up) ----------------------------------------------------
    posicao_dos_asteroides_em_y_up = 500
    posicao_dos_asteroides_em_y_up2 = 500
    posicao_dos_asteroides_em_y_up3 = 500
    posicao_dos_asteroides_em_x4 = random.randint(10, 280)
    posicao_dos_asteroides_em_x5 = random.randint(228, 416)
    posicao_dos_asteroides_em_x6 = random.randint(436, 630)

    # ----------------------------------------- asteroides à esquerda (Left) ------------------------------------------------
    posicao_dos_asteroides_em_x_left = 680
    posicao_dos_asteroides_em_x_left2 = 680
    posicao_dos_asteroides_em_x_left3 = 680
    posicao_dos_asteroides_em_y1 = random.randint(10, 130)
    posicao_dos_asteroides_em_y2 = random.randint(150, 300)
    posicao_dos_asteroides_em_y3 = random.randint(320, 480)

    # ------------------------------------------ asteroides à direita (Right) -----------------------------------------------
    posicao_dos_asteroides_em_x_right = -40
    posicao_dos_asteroides_em_x_right2 = -40
    posicao_dos_asteroides_em_x_right3 = -40
    posicao_dos_asteroides_em_y4 = random.randint(10, 130)
    posicao_dos_asteroides_em_y5 = random.randint(150, 300)
    posicao_dos_asteroides_em_y6 = random.randint(320, 480)

    # ------------------------------------------ recompensas ----------------------------------------------------------------
    posicao_da_recompensa_em_x = random.randint(30, 620)
    posicao_da_recompensa_em_y = random.randint(30, 460)
    score2 = 0

    # ------------------------------------------ velocidade do jogo ---------------------------------------------------------
    velocidadeDoJogo = 0

    musica()
    # -------------------------------------------- Loop Principal do jogo----------------------------------------------------
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.flip()

        # ----------------------------------------- asteroides que descem (41746491) --------------------------------------
        if velocidadeDoJogo >= 140:
            posicao_dos_asteroides_em_y_down += velocidade_do_asteroide
        if velocidadeDoJogo >= 1100:
            posicao_dos_asteroides_em_y_down2 += velocidade_do_asteroide
        if velocidadeDoJogo >= 2200:
            posicao_dos_asteroides_em_y_down3 += velocidade_do_asteroide

        # -----------------------------------------asteroides que sobem (Up) ------------------------------------------------
        if velocidadeDoJogo >= 600:
            posicao_dos_asteroides_em_y_up -= velocidade_do_asteroide
        if velocidadeDoJogo >= 1300:
            posicao_dos_asteroides_em_y_up2 -= velocidade_do_asteroide
        if velocidadeDoJogo >= 2200:
            posicao_dos_asteroides_em_y_up3 -= velocidade_do_asteroide

        # -----------------------------------------asteroides à esquerda (Left) ---------------------------------------------
        if velocidadeDoJogo >= 800:
            posicao_dos_asteroides_em_x_left -= velocidade_do_asteroide
        if velocidadeDoJogo >= 1500:
            posicao_dos_asteroides_em_x_left2 -= velocidade_do_asteroide

        if velocidadeDoJogo >= 2200:
            posicao_dos_asteroides_em_x_left3 -= velocidade_do_asteroide

        # -----------------------------------------asteroides à direita (Right) ---------------------------------------------
        if velocidadeDoJogo >= 1300:
            posicao_dos_asteroides_em_x_right += velocidade_do_asteroide
        if velocidadeDoJogo >= 1800:
            posicao_dos_asteroides_em_x_right2 += velocidade_do_asteroide
        if velocidadeDoJogo >= 2200:
            posicao_dos_asteroides_em_x_right3 += velocidade_do_asteroide


            # ------------------------------------------VELOCIDADE DO JOGO------------------------------------------------------
        if velocidadeDoJogo == 2200:
            fps
        elif velocidadeDoJogo >= 2200 and velocidadeDoJogo <= 4000:
            fps = 95
        elif velocidadeDoJogo >= 4000 and velocidadeDoJogo <= 6000:
            fps = 110
        elif velocidadeDoJogo >= 6000 and velocidadeDoJogo <= 8000:
            fps = 120
        elif velocidadeDoJogo >= 8000 and velocidadeDoJogo <= 10000:
            fps = 135
        elif velocidadeDoJogo >= 10000 and velocidadeDoJogo <= 12000:
            fps = 145
        elif velocidadeDoJogo >= 12000 and velocidadeDoJogo <= 14000:
            fps = 160
        elif velocidadeDoJogo >= 14000 and velocidadeDoJogo <= 16000:
            fps = 190
        elif velocidadeDoJogo >= 16000 and velocidadeDoJogo <= 20000:
            fps = 230
        elif velocidadeDoJogo > 20000:
            fps = 280
        relogio.tick(fps)

        # ----------------------------------------- Movimento Personagem ----------------------------------------------------
        tecla_pressionada = pygame.key.get_pressed()
        if tecla_pressionada[K_LEFT]:
            xpos -= movimento_em_x
            if xpos <= 0:
                xpos = 0

        if tecla_pressionada[K_RIGHT]:
            xpos += movimento_em_x
            if xpos >= 640:
                xpos = 640

        if tecla_pressionada[K_UP]:
            ypos -= movimento_em_y
            if ypos <= 0:
                ypos = 0

        if tecla_pressionada[K_DOWN]:
            ypos += movimento_em_y
            if ypos >= 480:
                ypos = 480


        # ------------------------------------------- Movimento Asteroides --------------------------------------------------
        elif posicao_dos_asteroides_em_y_down > 480:
            posicao_dos_asteroides_em_y_down = 0
            posicao_dos_asteroides_em_x = random.randint(10, 630)

        elif posicao_dos_asteroides_em_y_down2 > 480:
            posicao_dos_asteroides_em_y_down2 = 0
            posicao_dos_asteroides_em_x2 = random.randint(10, 630)

        elif posicao_dos_asteroides_em_y_down3 > 480:
            posicao_dos_asteroides_em_y_down3 = 0
            posicao_dos_asteroides_em_x3 = random.randint(10, 630)


        # -----------------------------------------  Movimento Asteroides ---------------------------------------------------
        elif posicao_dos_asteroides_em_y_up < 0:
            posicao_dos_asteroides_em_y_up = 480
            posicao_dos_asteroides_em_x4 = random.randint(10, 630)

        elif posicao_dos_asteroides_em_y_up2 < 0:
            posicao_dos_asteroides_em_y_up2 = 480
            posicao_dos_asteroides_em_x5 = random.randint(10, 630)

        elif posicao_dos_asteroides_em_y_up3 < 0:
            posicao_dos_asteroides_em_y_up3 = 480
            posicao_dos_asteroides_em_x6 = random.randint(10, 630)


        # ----------------------------------------- Movimento Asteroides  ---------------------------------------------------
        elif posicao_dos_asteroides_em_x_left < 0:
            posicao_dos_asteroides_em_x_left = 640
            posicao_dos_asteroides_em_y1 = random.randint(10, 130)

        elif posicao_dos_asteroides_em_x_left2 < 0:
            posicao_dos_asteroides_em_x_left2 = 640
            posicao_dos_asteroides_em_y2 = random.randint(150, 300)

        elif posicao_dos_asteroides_em_x_left3 < 0:
            posicao_dos_asteroides_em_x_left3 = 640
            posicao_dos_asteroides_em_y3 = random.randint(320, 480)


        # ----------------------------------------- Movimento Asteroides  --------------------------------------------------
        elif posicao_dos_asteroides_em_x_right > 640:
            posicao_dos_asteroides_em_x_right = 0
            posicao_dos_asteroides_em_y4 = random.randint(10, 130)

        elif posicao_dos_asteroides_em_x_right2 > 640:
            posicao_dos_asteroides_em_x_right2 = 0
            posicao_dos_asteroides_em_y5 = random.randint(150, 300)

        elif posicao_dos_asteroides_em_x_right3 > 640:
            posicao_dos_asteroides_em_x_right3 = 0
            posicao_dos_asteroides_em_y6 = random.randint(320, 480)


        # -----------------------------------------  fundo da tela ---------------------------------------------------------
        ecra.fill(branco)


        # ---------------------------------------- Circulo Azul ( personagem) ----------------------------------------------
        circulo = pygame.draw.circle(ecra, preto, (xpos, ypos), raio_circulo)


        # ------------------------------------------ recompensas -----------------------------------------------------------
        recompensa = pygame.draw.circle(ecra, azul, (posicao_da_recompensa_em_x, posicao_da_recompensa_em_y), raio_circulo)


        # ------------------------------------ Asteroids fase1 -------------------------------------------------------------
        asteroide = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x, posicao_dos_asteroides_em_y_down), raio_circulo)
        asteroide2 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x2, posicao_dos_asteroides_em_y_down2), raio_circulo)
        asteroide3 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x3, posicao_dos_asteroides_em_y_down3),raio_circulo)


        # ------------------------------------ Asteroids fase2 -------------------------------------------------------------
        asteroide4 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x4, posicao_dos_asteroides_em_y_up),
                                        raio_circulo)
        asteroide5 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x5, posicao_dos_asteroides_em_y_up2),
                                        raio_circulo)
        asteroide6 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x6, posicao_dos_asteroides_em_y_up3),
                                        raio_circulo)


        # ------------------------------------ Asteroids fase3 -------------------------------------------------------------
        asteroide7 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_left, posicao_dos_asteroides_em_y1),
                                        raio_circulo)
        asteroide8 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_left2, posicao_dos_asteroides_em_y2),
                                        raio_circulo)
        asteroide9 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_left3, posicao_dos_asteroides_em_y3),
                                        raio_circulo)


        # ------------------------------------ Asteroids fase4 -------------------------------------------------------------
        asteroide10 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_right, posicao_dos_asteroides_em_y4),
                                         raio_circulo)
        asteroide11 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_right2, posicao_dos_asteroides_em_y5),
                                         raio_circulo)
        asteroide12 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_right3, posicao_dos_asteroides_em_y6),
                                         raio_circulo)


        # -------------------------------------------------- Vidas ----------------------------------------------------------
        if vida == 3:
            vida1 = ecra.blit(imgvida, [20, 10])
            vida2 = ecra.blit(imgvida, [40, 10])
            vida3 = ecra.blit(imgvida, [60, 10])
        elif vida == 2:
            vida1 = ecra.blit(imgvida, [20, 10])
            vida2 = ecra.blit(imgvida, [40, 10])
        elif vida == 1:
            vida1 = ecra.blit(imgvida, [20, 10])

        # ------------------------------------------------- detectando colisão ---------------------------------------------
        if circulo.colliderect(asteroide):
            vida -= 1
            time.sleep(0.6)
            xpos = 320
            ypos = 240

            # --------------------------------------- asteroides que descem (down) --------------------------------------------------
            posicao_dos_asteroides_em_x = random.randint(10, 208)
            posicao_dos_asteroides_em_x2 = random.randint(228, 416)
            posicao_dos_asteroides_em_x3 = random.randint(436, 630)
            posicao_dos_asteroides_em_y_down = -20
            posicao_dos_asteroides_em_y_down2 = -20
            posicao_dos_asteroides_em_y_down3 = -20

            # ---------------------------------------- asteroides que sobem (Up) ----------------------------------------------------
            posicao_dos_asteroides_em_y_up = 500
            posicao_dos_asteroides_em_y_up2 = 500
            posicao_dos_asteroides_em_y_up3 = 500
            posicao_dos_asteroides_em_x4 = random.randint(10, 280)
            posicao_dos_asteroides_em_x5 = random.randint(228, 416)
            posicao_dos_asteroides_em_x6 = random.randint(436, 630)

            # ----------------------------------------- asteroides à esquerda (Left) ------------------------------------------------
            posicao_dos_asteroides_em_x_left = 680
            posicao_dos_asteroides_em_x_left2 = 680
            posicao_dos_asteroides_em_x_left3 = 680
            posicao_dos_asteroides_em_y1 = random.randint(10, 130)
            posicao_dos_asteroides_em_y2 = random.randint(150, 300)
            posicao_dos_asteroides_em_y3 = random.randint(320, 480)

            # ------------------------------------------ asteroides à direita (Right) -----------------------------------------------
            posicao_dos_asteroides_em_x_right = -40
            posicao_dos_asteroides_em_x_right2 = -40
            posicao_dos_asteroides_em_x_right3 = -40
            posicao_dos_asteroides_em_y4 = random.randint(10, 130)
            posicao_dos_asteroides_em_y5 = random.randint(150, 300)
            posicao_dos_asteroides_em_y6 = random.randint(320, 480)

            # ------------------------------------------ recompensas ----------------------------------------------------------------
            posicao_da_recompensa_em_x = random.randint(30, 620)
            posicao_da_recompensa_em_y = random.randint(30, 460)
            if vida == 0:
                vivo = False
                break
                pygame.mixer.music.play()

        elif circulo.colliderect(asteroide2):
            vida -= 1
            time.sleep(0.6)
            xpos = 320
            ypos = 240
            # --------------------------------------- asteroides que descem (down) --------------------------------------------------
            posicao_dos_asteroides_em_x = random.randint(10, 208)
            posicao_dos_asteroides_em_x2 = random.randint(228, 416)
            posicao_dos_asteroides_em_x3 = random.randint(436, 630)
            posicao_dos_asteroides_em_y_down = -20
            posicao_dos_asteroides_em_y_down2 = -20
            posicao_dos_asteroides_em_y_down3 = -20

            # ---------------------------------------- asteroides que sobem (Up) ----------------------------------------------------
            posicao_dos_asteroides_em_y_up = 500
            posicao_dos_asteroides_em_y_up2 = 500
            posicao_dos_asteroides_em_y_up3 = 500
            posicao_dos_asteroides_em_x4 = random.randint(10, 280)
            posicao_dos_asteroides_em_x5 = random.randint(228, 416)
            posicao_dos_asteroides_em_x6 = random.randint(436, 630)

            # ----------------------------------------- asteroides à esquerda (Left) ------------------------------------------------
            posicao_dos_asteroides_em_x_left = 680
            posicao_dos_asteroides_em_x_left2 = 680
            posicao_dos_asteroides_em_x_left3 = 680
            posicao_dos_asteroides_em_y1 = random.randint(10, 130)
            posicao_dos_asteroides_em_y2 = random.randint(150, 300)
            posicao_dos_asteroides_em_y3 = random.randint(320, 480)

            # ------------------------------------------ asteroides à direita (Right) -----------------------------------------------
            posicao_dos_asteroides_em_x_right = -40
            posicao_dos_asteroides_em_x_right2 = -40
            posicao_dos_asteroides_em_x_right3 = -40
            posicao_dos_asteroides_em_y4 = random.randint(10, 130)
            posicao_dos_asteroides_em_y5 = random.randint(150, 300)
            posicao_dos_asteroides_em_y6 = random.randint(320, 480)

            # ------------------------------------------ recompensas ----------------------------------------------------------------
            posicao_da_recompensa_em_x = random.randint(30, 620)
            posicao_da_recompensa_em_y = random.randint(30, 460)
            if vida <= 0:
                vivo = False

                break
                pygame.mixer.music.play()

        elif circulo.colliderect(asteroide3):
            vida -= 1
            time.sleep(0.6)
            xpos = 320
            ypos = 240
            # --------------------------------------- asteroides que descem (down) --------------------------------------------------
            posicao_dos_asteroides_em_x = random.randint(10, 208)
            posicao_dos_asteroides_em_x2 = random.randint(228, 416)
            posicao_dos_asteroides_em_x3 = random.randint(436, 630)
            posicao_dos_asteroides_em_y_down = -20
            posicao_dos_asteroides_em_y_down2 = -20
            posicao_dos_asteroides_em_y_down3 = -20

            # ---------------------------------------- asteroides que sobem (Up) ----------------------------------------------------
            posicao_dos_asteroides_em_y_up = 500
            posicao_dos_asteroides_em_y_up2 = 500
            posicao_dos_asteroides_em_y_up3 = 500
            posicao_dos_asteroides_em_x4 = random.randint(10, 280)
            posicao_dos_asteroides_em_x5 = random.randint(228, 416)
            posicao_dos_asteroides_em_x6 = random.randint(436, 630)

            # ----------------------------------------- asteroides à esquerda (Left) ------------------------------------------------
            posicao_dos_asteroides_em_x_left = 680
            posicao_dos_asteroides_em_x_left2 = 680
            posicao_dos_asteroides_em_x_left3 = 680
            posicao_dos_asteroides_em_y1 = random.randint(10, 130)
            posicao_dos_asteroides_em_y2 = random.randint(150, 300)
            posicao_dos_asteroides_em_y3 = random.randint(320, 480)

            # ------------------------------------------ asteroides à direita (Right) -----------------------------------------------
            posicao_dos_asteroides_em_x_right = -40
            posicao_dos_asteroides_em_x_right2 = -40
            posicao_dos_asteroides_em_x_right3 = -40
            posicao_dos_asteroides_em_y4 = random.randint(10, 130)
            posicao_dos_asteroides_em_y5 = random.randint(150, 300)
            posicao_dos_asteroides_em_y6 = random.randint(320, 480)

            # ------------------------------------------ recompensas ----------------------------------------------------------------
            posicao_da_recompensa_em_x = random.randint(30, 620)
            posicao_da_recompensa_em_y = random.randint(30, 460)
            if vida <= 0:
                vivo = False
                break
                pygame.mixer.music.play()

        elif circulo.colliderect(asteroide4):
            vida -= 1
            time.sleep(0.6)
            xpos = 320
            ypos = 240
            # --------------------------------------- asteroides que descem (down) --------------------------------------------------
            posicao_dos_asteroides_em_x = random.randint(10, 208)
            posicao_dos_asteroides_em_x2 = random.randint(228, 416)
            posicao_dos_asteroides_em_x3 = random.randint(436, 630)
            posicao_dos_asteroides_em_y_down = -20
            posicao_dos_asteroides_em_y_down2 = -20
            posicao_dos_asteroides_em_y_down3 = -20

            # ---------------------------------------- asteroides que sobem (Up) ----------------------------------------------------
            posicao_dos_asteroides_em_y_up = 500
            posicao_dos_asteroides_em_y_up2 = 500
            posicao_dos_asteroides_em_y_up3 = 500
            posicao_dos_asteroides_em_x4 = random.randint(10, 280)
            posicao_dos_asteroides_em_x5 = random.randint(228, 416)
            posicao_dos_asteroides_em_x6 = random.randint(436, 630)

            # ----------------------------------------- asteroides à esquerda (Left) ------------------------------------------------
            posicao_dos_asteroides_em_x_left = 680
            posicao_dos_asteroides_em_x_left2 = 680
            posicao_dos_asteroides_em_x_left3 = 680
            posicao_dos_asteroides_em_y1 = random.randint(10, 130)
            posicao_dos_asteroides_em_y2 = random.randint(150, 300)
            posicao_dos_asteroides_em_y3 = random.randint(320, 480)

            # ------------------------------------------ asteroides à direita (Right) -----------------------------------------------
            posicao_dos_asteroides_em_x_right = -40
            posicao_dos_asteroides_em_x_right2 = -40
            posicao_dos_asteroides_em_x_right3 = -40
            posicao_dos_asteroides_em_y4 = random.randint(10, 130)
            posicao_dos_asteroides_em_y5 = random.randint(150, 300)
            posicao_dos_asteroides_em_y6 = random.randint(320, 480)

            # ------------------------------------------ recompensas ----------------------------------------------------------------
            posicao_da_recompensa_em_x = random.randint(30, 620)
            posicao_da_recompensa_em_y = random.randint(30, 460)

            if vida <= 0:
                vivo = False
                break
                pygame.mixer.music.play()

        elif circulo.colliderect(asteroide5):
            vida -= 1
            time.sleep(0.6)
            xpos = 320
            ypos = 240
            # --------------------------------------- asteroides que descem (down) --------------------------------------------------
            posicao_dos_asteroides_em_x = random.randint(10, 208)
            posicao_dos_asteroides_em_x2 = random.randint(228, 416)
            posicao_dos_asteroides_em_x3 = random.randint(436, 630)
            posicao_dos_asteroides_em_y_down = -20
            posicao_dos_asteroides_em_y_down2 = -20
            posicao_dos_asteroides_em_y_down3 = -20

            # ---------------------------------------- asteroides que sobem (Up) ----------------------------------------------------
            posicao_dos_asteroides_em_y_up = 500
            posicao_dos_asteroides_em_y_up2 = 500
            posicao_dos_asteroides_em_y_up3 = 500
            posicao_dos_asteroides_em_x4 = random.randint(10, 280)
            posicao_dos_asteroides_em_x5 = random.randint(228, 416)
            posicao_dos_asteroides_em_x6 = random.randint(436, 630)

            # ----------------------------------------- asteroides à esquerda (Left) ------------------------------------------------
            posicao_dos_asteroides_em_x_left = 680
            posicao_dos_asteroides_em_x_left2 = 680
            posicao_dos_asteroides_em_x_left3 = 680
            posicao_dos_asteroides_em_y1 = random.randint(10, 130)
            posicao_dos_asteroides_em_y2 = random.randint(150, 300)
            posicao_dos_asteroides_em_y3 = random.randint(320, 480)

            # ------------------------------------------ asteroides à direita (Right) -----------------------------------------------
            posicao_dos_asteroides_em_x_right = -40
            posicao_dos_asteroides_em_x_right2 = -40
            posicao_dos_asteroides_em_x_right3 = -40
            posicao_dos_asteroides_em_y4 = random.randint(10, 130)
            posicao_dos_asteroides_em_y5 = random.randint(150, 300)
            posicao_dos_asteroides_em_y6 = random.randint(320, 480)

            # ------------------------------------------ recompensas ----------------------------------------------------------------
            posicao_da_recompensa_em_x = random.randint(30, 620)
            posicao_da_recompensa_em_y = random.randint(30, 460)

            if vida <= 0:
                vivo = False
                break
                pygame.mixer.music.play()

        elif circulo.colliderect(asteroide6):
            vida -= 1
            time.sleep(0.6)
            xpos = 320
            ypos = 240
            # --------------------------------------- asteroides que descem (down) --------------------------------------------------
            posicao_dos_asteroides_em_x = random.randint(10, 208)
            posicao_dos_asteroides_em_x2 = random.randint(228, 416)
            posicao_dos_asteroides_em_x3 = random.randint(436, 630)
            posicao_dos_asteroides_em_y_down = -20
            posicao_dos_asteroides_em_y_down2 = -20
            posicao_dos_asteroides_em_y_down3 = -20

            # ---------------------------------------- asteroides que sobem (Up) ----------------------------------------------------
            posicao_dos_asteroides_em_y_up = 500
            posicao_dos_asteroides_em_y_up2 = 500
            posicao_dos_asteroides_em_y_up3 = 500
            posicao_dos_asteroides_em_x4 = random.randint(10, 280)
            posicao_dos_asteroides_em_x5 = random.randint(228, 416)
            posicao_dos_asteroides_em_x6 = random.randint(436, 630)

            # ----------------------------------------- asteroides à esquerda (Left) ------------------------------------------------
            posicao_dos_asteroides_em_x_left = 680
            posicao_dos_asteroides_em_x_left2 = 680
            posicao_dos_asteroides_em_x_left3 = 680
            posicao_dos_asteroides_em_y1 = random.randint(10, 130)
            posicao_dos_asteroides_em_y2 = random.randint(150, 300)
            posicao_dos_asteroides_em_y3 = random.randint(320, 480)

            # ------------------------------------------ asteroides à direita (Right) -----------------------------------------------
            posicao_dos_asteroides_em_x_right = -40
            posicao_dos_asteroides_em_x_right2 = -40
            posicao_dos_asteroides_em_x_right3 = -40
            posicao_dos_asteroides_em_y4 = random.randint(10, 130)
            posicao_dos_asteroides_em_y5 = random.randint(150, 300)
            posicao_dos_asteroides_em_y6 = random.randint(320, 480)

            # ------------------------------------------ recompensas ----------------------------------------------------------------
            posicao_da_recompensa_em_x = random.randint(30, 620)
            posicao_da_recompensa_em_y = random.randint(30, 460)

            if vida <= 0:
                vivo = False
                break
                pygame.mixer.music.play()

        elif circulo.colliderect(asteroide7):
            vida -= 1
            time.sleep(0.6)
            xpos = 320
            ypos = 240
            # --------------------------------------- asteroides que descem (down) --------------------------------------------------
            posicao_dos_asteroides_em_x = random.randint(10, 208)
            posicao_dos_asteroides_em_x2 = random.randint(228, 416)
            posicao_dos_asteroides_em_x3 = random.randint(436, 630)
            posicao_dos_asteroides_em_y_down = -20
            posicao_dos_asteroides_em_y_down2 = -20
            posicao_dos_asteroides_em_y_down3 = -20

            # ---------------------------------------- asteroides que sobem (Up) ----------------------------------------------------
            posicao_dos_asteroides_em_y_up = 500
            posicao_dos_asteroides_em_y_up2 = 500
            posicao_dos_asteroides_em_y_up3 = 500
            posicao_dos_asteroides_em_x4 = random.randint(10, 280)
            posicao_dos_asteroides_em_x5 = random.randint(228, 416)
            posicao_dos_asteroides_em_x6 = random.randint(436, 630)

            # ----------------------------------------- asteroides à esquerda (Left) ------------------------------------------------
            posicao_dos_asteroides_em_x_left = 680
            posicao_dos_asteroides_em_x_left2 = 680
            posicao_dos_asteroides_em_x_left3 = 680
            posicao_dos_asteroides_em_y1 = random.randint(10, 130)
            posicao_dos_asteroides_em_y2 = random.randint(150, 300)
            posicao_dos_asteroides_em_y3 = random.randint(320, 480)

            # ------------------------------------------ asteroides à direita (Right) -----------------------------------------------
            posicao_dos_asteroides_em_x_right = -40
            posicao_dos_asteroides_em_x_right2 = -40
            posicao_dos_asteroides_em_x_right3 = -40
            posicao_dos_asteroides_em_y4 = random.randint(10, 130)
            posicao_dos_asteroides_em_y5 = random.randint(150, 300)
            posicao_dos_asteroides_em_y6 = random.randint(320, 480)

            # ------------------------------------------ recompensas ----------------------------------------------------------------
            posicao_da_recompensa_em_x = random.randint(30, 620)
            posicao_da_recompensa_em_y = random.randint(30, 460)

            if vida <= 0:
                vivo = False
                break
                pygame.mixer.music.stop()

        elif circulo.colliderect(asteroide8):
            vida -= 1
            time.sleep(0.6)
            xpos = 320
            ypos = 240
            # --------------------------------------- asteroides que descem (down) --------------------------------------------------
            posicao_dos_asteroides_em_x = random.randint(10, 208)
            posicao_dos_asteroides_em_x2 = random.randint(228, 416)
            posicao_dos_asteroides_em_x3 = random.randint(436, 630)
            posicao_dos_asteroides_em_y_down = -20
            posicao_dos_asteroides_em_y_down2 = -20
            posicao_dos_asteroides_em_y_down3 = -20

            # ---------------------------------------- asteroides que sobem (Up) ----------------------------------------------------
            posicao_dos_asteroides_em_y_up = 500
            posicao_dos_asteroides_em_y_up2 = 500
            posicao_dos_asteroides_em_y_up3 = 500
            posicao_dos_asteroides_em_x4 = random.randint(10, 280)
            posicao_dos_asteroides_em_x5 = random.randint(228, 416)
            posicao_dos_asteroides_em_x6 = random.randint(436, 630)

            # ----------------------------------------- asteroides à esquerda (Left) ------------------------------------------------
            posicao_dos_asteroides_em_x_left = 680
            posicao_dos_asteroides_em_x_left2 = 680
            posicao_dos_asteroides_em_x_left3 = 680
            posicao_dos_asteroides_em_y1 = random.randint(10, 130)
            posicao_dos_asteroides_em_y2 = random.randint(150, 300)
            posicao_dos_asteroides_em_y3 = random.randint(320, 480)

            # ------------------------------------------ asteroides à direita (Right) -----------------------------------------------
            posicao_dos_asteroides_em_x_right = -40
            posicao_dos_asteroides_em_x_right2 = -40
            posicao_dos_asteroides_em_x_right3 = -40
            posicao_dos_asteroides_em_y4 = random.randint(10, 130)
            posicao_dos_asteroides_em_y5 = random.randint(150, 300)
            posicao_dos_asteroides_em_y6 = random.randint(320, 480)

            # ------------------------------------------ recompensas ----------------------------------------------------------------
            posicao_da_recompensa_em_x = random.randint(30, 620)
            posicao_da_recompensa_em_y = random.randint(30, 460)

            if vida <= 0:
                vivo = False
                break
                pygame.mixer.music.play()

        elif circulo.colliderect(asteroide9):
            vida -= 1
            time.sleep(0.6)
            xpos = 320
            ypos = 240
            # --------------------------------------- asteroides que descem (down) --------------------------------------------------
            posicao_dos_asteroides_em_x = random.randint(10, 208)
            posicao_dos_asteroides_em_x2 = random.randint(228, 416)
            posicao_dos_asteroides_em_x3 = random.randint(436, 630)
            posicao_dos_asteroides_em_y_down = -20
            posicao_dos_asteroides_em_y_down2 = -20
            posicao_dos_asteroides_em_y_down3 = -20

            # ---------------------------------------- asteroides que sobem (Up) ----------------------------------------------------
            posicao_dos_asteroides_em_y_up = 500
            posicao_dos_asteroides_em_y_up2 = 500
            posicao_dos_asteroides_em_y_up3 = 500
            posicao_dos_asteroides_em_x4 = random.randint(10, 280)
            posicao_dos_asteroides_em_x5 = random.randint(228, 416)
            posicao_dos_asteroides_em_x6 = random.randint(436, 630)

            # ----------------------------------------- asteroides à esquerda (Left) ------------------------------------------------
            posicao_dos_asteroides_em_x_left = 680
            posicao_dos_asteroides_em_x_left2 = 680
            posicao_dos_asteroides_em_x_left3 = 680
            posicao_dos_asteroides_em_y1 = random.randint(10, 130)
            posicao_dos_asteroides_em_y2 = random.randint(150, 300)
            posicao_dos_asteroides_em_y3 = random.randint(320, 480)

            # ------------------------------------------ asteroides à direita (Right) -----------------------------------------------
            posicao_dos_asteroides_em_x_right = -40
            posicao_dos_asteroides_em_x_right2 = -40
            posicao_dos_asteroides_em_x_right3 = -40
            posicao_dos_asteroides_em_y4 = random.randint(10, 130)
            posicao_dos_asteroides_em_y5 = random.randint(150, 300)
            posicao_dos_asteroides_em_y6 = random.randint(320, 480)

            # ------------------------------------------ recompensas ----------------------------------------------------------------
            posicao_da_recompensa_em_x = random.randint(30, 620)
            posicao_da_recompensa_em_y = random.randint(30, 460)
            if vida <= 0:
                vivo = False
                break
                pygame.mixer.music.play()

        elif circulo.colliderect(asteroide10):
            vida -= 1
            time.sleep(0.6)
            xpos = 320
            ypos = 240
            # --------------------------------------- asteroides que descem (down) --------------------------------------------------
            posicao_dos_asteroides_em_x = random.randint(10, 208)
            posicao_dos_asteroides_em_x2 = random.randint(228, 416)
            posicao_dos_asteroides_em_x3 = random.randint(436, 630)
            posicao_dos_asteroides_em_y_down = -20
            posicao_dos_asteroides_em_y_down2 = -20
            posicao_dos_asteroides_em_y_down3 = -20

            # ---------------------------------------- asteroides que sobem (Up) ----------------------------------------------------
            posicao_dos_asteroides_em_y_up = 500
            posicao_dos_asteroides_em_y_up2 = 500
            posicao_dos_asteroides_em_y_up3 = 500
            posicao_dos_asteroides_em_x4 = random.randint(10, 280)
            posicao_dos_asteroides_em_x5 = random.randint(228, 416)
            posicao_dos_asteroides_em_x6 = random.randint(436, 630)

            # ----------------------------------------- asteroides à esquerda (Left) ------------------------------------------------
            posicao_dos_asteroides_em_x_left = 680
            posicao_dos_asteroides_em_x_left2 = 680
            posicao_dos_asteroides_em_x_left3 = 680
            posicao_dos_asteroides_em_y1 = random.randint(10, 130)
            posicao_dos_asteroides_em_y2 = random.randint(150, 300)
            posicao_dos_asteroides_em_y3 = random.randint(320, 480)

            # ------------------------------------------ asteroides à direita (Right) -----------------------------------------------
            posicao_dos_asteroides_em_x_right = -40
            posicao_dos_asteroides_em_x_right2 = -40
            posicao_dos_asteroides_em_x_right3 = -40
            posicao_dos_asteroides_em_y4 = random.randint(10, 130)
            posicao_dos_asteroides_em_y5 = random.randint(150, 300)
            posicao_dos_asteroides_em_y6 = random.randint(320, 480)

            # ------------------------------------------ recompensas ----------------------------------------------------------------
            posicao_da_recompensa_em_x = random.randint(30, 620)
            posicao_da_recompensa_em_y = random.randint(30, 460)

            if vida <= 0:
                vivo = False
                break
                pygame.mixer.music.play()

        elif circulo.colliderect(asteroide11):
            vida -= 1
            time.sleep(0.6)
            xpos = 320
            ypos = 240
            # --------------------------------------- asteroides que descem (down) --------------------------------------------------
            posicao_dos_asteroides_em_x = random.randint(10, 208)
            posicao_dos_asteroides_em_x2 = random.randint(228, 416)
            posicao_dos_asteroides_em_x3 = random.randint(436, 630)
            posicao_dos_asteroides_em_y_down = -20
            posicao_dos_asteroides_em_y_down2 = -20
            posicao_dos_asteroides_em_y_down3 = -20

            # ---------------------------------------- asteroides que sobem (Up) ----------------------------------------------------
            posicao_dos_asteroides_em_y_up = 500
            posicao_dos_asteroides_em_y_up2 = 500
            posicao_dos_asteroides_em_y_up3 = 500
            posicao_dos_asteroides_em_x4 = random.randint(10, 280)
            posicao_dos_asteroides_em_x5 = random.randint(228, 416)
            posicao_dos_asteroides_em_x6 = random.randint(436, 630)

            # ----------------------------------------- asteroides à esquerda (Left) ------------------------------------------------
            posicao_dos_asteroides_em_x_left = 680
            posicao_dos_asteroides_em_x_left2 = 680
            posicao_dos_asteroides_em_x_left3 = 680
            posicao_dos_asteroides_em_y1 = random.randint(10, 130)
            posicao_dos_asteroides_em_y2 = random.randint(150, 300)
            posicao_dos_asteroides_em_y3 = random.randint(320, 480)

            # ------------------------------------------ asteroides à direita (Right) -----------------------------------------------
            posicao_dos_asteroides_em_x_right = -40
            posicao_dos_asteroides_em_x_right2 = -40
            posicao_dos_asteroides_em_x_right3 = -40
            posicao_dos_asteroides_em_y4 = random.randint(10, 130)
            posicao_dos_asteroides_em_y5 = random.randint(150, 300)
            posicao_dos_asteroides_em_y6 = random.randint(320, 480)

            # ------------------------------------------ recompensas ----------------------------------------------------------------
            posicao_da_recompensa_em_x = random.randint(30, 620)
            posicao_da_recompensa_em_y = random.randint(30, 460)

            if vida <= 0:
                vivo = False
                break
                pygame.mixer.music.play()

        elif circulo.colliderect(asteroide12):
            vida -= 1
            time.sleep(0.6)
            xpos = 320
            ypos = 240
            # --------------------------------------- asteroides que descem (down) --------------------------------------------------
            posicao_dos_asteroides_em_x = random.randint(10, 208)
            posicao_dos_asteroides_em_x2 = random.randint(228, 416)
            posicao_dos_asteroides_em_x3 = random.randint(436, 630)
            posicao_dos_asteroides_em_y_down = -20
            posicao_dos_asteroides_em_y_down2 = -20
            posicao_dos_asteroides_em_y_down3 = -20

            # ---------------------------------------- asteroides que sobem (Up) ----------------------------------------------------
            posicao_dos_asteroides_em_y_up = 500
            posicao_dos_asteroides_em_y_up2 = 500
            posicao_dos_asteroides_em_y_up3 = 500
            posicao_dos_asteroides_em_x4 = random.randint(10, 280)
            posicao_dos_asteroides_em_x5 = random.randint(228, 416)
            posicao_dos_asteroides_em_x6 = random.randint(436, 630)

            # ----------------------------------------- asteroides à esquerda (Left) ------------------------------------------------
            posicao_dos_asteroides_em_x_left = 680
            posicao_dos_asteroides_em_x_left2 = 680
            posicao_dos_asteroides_em_x_left3 = 680
            posicao_dos_asteroides_em_y1 = random.randint(10, 130)
            posicao_dos_asteroides_em_y2 = random.randint(150, 300)
            posicao_dos_asteroides_em_y3 = random.randint(320, 480)

            # ------------------------------------------ asteroides à direita (Right) -----------------------------------------------
            posicao_dos_asteroides_em_x_right = -40
            posicao_dos_asteroides_em_x_right2 = -40
            posicao_dos_asteroides_em_x_right3 = -40
            posicao_dos_asteroides_em_y4 = random.randint(10, 130)
            posicao_dos_asteroides_em_y5 = random.randint(150, 300)
            posicao_dos_asteroides_em_y6 = random.randint(320, 480)

            # ------------------------------------------ recompensas ----------------------------------------------------------------
            posicao_da_recompensa_em_x = random.randint(30, 620)
            posicao_da_recompensa_em_y = random.randint(30, 460)

            if vida <= 0:
                vivo = False
                break
                pygame.mixer.music.play()



        # ------------------------------------------- Score ----------------------------------------------------------------

        velocidadeDoJogo += 1
        score = velocidadeDoJogo
        fonte = pygame.font.Font(None, 30)
        pontuacao = fonte.render('Pontuação: ' + str(score+score2), 2, preto)
        caixadepontuacao = pontuacao.get_rect()
        ecra.blit(pontuacao, [435, 10])
        potuacao1 = score+score2
        if potuacao1 > pontuacao_final:
            pontuacao_final = potuacao1
        # ------------------------------------------- Recompensa ----41706692-------------------------------------------------
        if circulo.colliderect(recompensa):
            posicao_da_recompensa_em_x = random.randint(25, 620)
            posicao_da_recompensa_em_y = random.randint(25, 460)
            score2 += 1000

posicao_do_select = 271

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()



    tecla_pressionada = pygame.key.get_pressed()

    if tecla_pressionada[K_BACKSPACE]:
        pygame.quit()
    if tecla_pressionada[K_DOWN]:
        if posicao_do_select == 271:
                posicao_do_select += 65

    if tecla_pressionada[K_UP]:
        if posicao_do_select == 336:
                posicao_do_select -= 65
    if posicao_do_select == 271 and tecla_pressionada[K_SPACE]:
        inst()

    if  posicao_do_select == 336 and tecla_pressionada[K_SPACE]:
        jogo()

    if vivo == False:
        morte()
        verificador = True
        pontuacao1 = 0
    if vivo == True and verificador == True:
        jogo()


    pygame.display.flip()
    bg = pygame.image.load('IMG/bg.png')
    logo = pygame.image.load('IMG/logo.png')
    botao_instrucao = pygame.image.load('IMG/botao_instrucao.png')
    botao_entrar = pygame.image.load('IMG/botao_entrar.png')
    selecionar_botao = pygame.image.load('IMG/select.png')

    ecra.blit(bg, (0, 0))
    ecra.blit(botao_instrucao, (180, 260))
    ecra.blit(botao_entrar, (180, 320))
    ecra.blit(logo, (230, 30))

    ecra.blit(selecionar_botao, (120, posicao_do_select))
    pygame.display.flip()

pygame.quit()
