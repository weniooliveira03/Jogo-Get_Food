import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 400
altura = 600

x_personagem = 160

x_comida = (randint(0, 9)) * 40
y_comida = 0
velocidade = 6
aumento_velocidade = 2
dificuldade = 'MÉDIA'
cores_comida = ((255, 0, 0), (255, 0, 127), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (127, 0, 255), (0, 125, 0))
cores_sombra_comida = ((175, 0, 0), (175, 0, 87), (200, 87, 0), (175, 175, 0), (0, 175, 0), (0, 175, 175), (87, 0, 175), (0, 100, 0))
cor = randint(0, 6)

pontos = 0
level_pontos = 0
erros = 0

tela = pygame.display.set_mode((largura, altura))
cor_tela = (50, 30, 60)
pygame.display.set_caption('Get Food')

relogio = pygame.time.Clock()

perdeu = False

iniciar = False


def exibir_texto(nome_fonte = 'arial',
                 tamanho_fonte = 20,
                 negrito = False,
                 italico = False,
                 texto = 'Texto',
                 cor_texto = (255, 255, 255),
                 cor_background = (None),
                 posicao_texto = (0, 0)
                 ):
    fonte = pygame.font.SysFont(nome_fonte, tamanho_fonte, negrito, italico)
    texto_formatado = fonte.render(texto, True, cor_texto, cor_background)
    tela.blit(texto_formatado, (posicao_texto), None, 0)


def botao(cor_botao = (0, 255, 0),
          posicao_tamanho =  (0, 0, 100, 50),
          texto_botao = 'Botão',
          cor_mensagem = (255, 255, 255),
          posicao_texto = (0,0),
          tamanho_texto = 20
          ):

    exibir_sombra_botao = pygame.draw.rect(tela, (cor_botao[0] + 40, cor_botao[1] + 40, cor_botao[2] + 40), (posicao_tamanho))

    exibir_botao = pygame.draw.rect(tela, (cor_botao), (posicao_tamanho[0] + 5, posicao_tamanho[1] + 5, posicao_tamanho[2] - 10, posicao_tamanho[3] - 10))
    texto_botao = texto_botao

    exibir_texto(
        tamanho_fonte= tamanho_texto,
        negrito = True,
        texto = texto_botao,
        cor_texto = (cor_mensagem),
        cor_background = (cor_botao),
        posicao_texto = (posicao_texto)
        )

    if event.type == MOUSEBUTTONDOWN:
        if event.button == BUTTON_LEFT:
            if exibir_sombra_botao.collidepoint(event.pos):
                exibir_sombra_botao = pygame.draw.rect(tela, (cor_botao[0] + 40, cor_botao[1] + 40, cor_botao[2] + 40), (posicao_tamanho[0] - 5, posicao_tamanho[1] -5, posicao_tamanho[2] + 10, posicao_tamanho[3] + 10))
                exibir_botao = pygame.draw.rect(tela, (cor_botao), (posicao_tamanho[0], posicao_tamanho[1], posicao_tamanho[2], posicao_tamanho[3]))
                exibir_texto(
                 negrito = True,
                 tamanho_fonte = tamanho_texto,
                 texto = texto_botao,
                 cor_texto = (cor_mensagem),
                 cor_background = (cor_botao),
                 posicao_texto = (posicao_texto)
                 )
    texto_botao = texto_botao
    if event.type == MOUSEBUTTONUP:
        if event.button == BUTTON_LEFT:
            if exibir_sombra_botao.collidepoint(event.pos):
                return True
            

def reiniciar():
    global pontos, erros, perdeu, velocidade, level_pontos, iniciar
    pontos = 0
    erros = 0
    perdeu = False
    if dificuldade == 'FÁCIL':
        velocidade = 4
    elif dificuldade == 'MÉDIO':
        velocidade = 6
    else:
        velocidade = 8
    level_pontos = 0

def tela_inicio():
    global iniciar

    iniciar = False
    reiniciar()

def tela_dificuldade():
    global dificuldade, velocidade, aumento_velocidade, tela_dificudade_ativa
    tela.fill((cor_tela))

    if botao(
        cor_botao = (0, 130, 0),
        posicao_tamanho = (100, 215, 200, 50),
        texto_botao = 'FÁCIL',
        cor_mensagem = (255, 255, 255),
        posicao_texto = (170, 230)
        ):
        dificuldade = 'FÁCIL'
        velocidade = 4
        aumento_velocidade = 1
        tela_dificudade_ativa = False
        
    if botao(
        cor_botao = (130, 130, 0),
        posicao_tamanho = (100, 275, 200, 50),
        texto_botao = 'MÉDIO',
        cor_mensagem = (255, 255, 255),
        posicao_texto = (165, 290)
        ):
        dificuldade = 'MÉDIO'
        velocidade = 6
        aumento_velocidade = 2
        tela_dificudade_ativa = False

    if botao(
        cor_botao = (130, 0, 0),
        posicao_tamanho = (100, 335, 200, 50),
        texto_botao = 'DIFICIL',
        cor_mensagem = (255, 255, 255),
        posicao_texto = (165, 350)
        ):
        dificuldade = 'DIFÍCIL'
        velocidade = 8
        aumento_velocidade = 3
        tela_dificudade_ativa = False
    

while True:
    tela.fill((cor_tela))

    exibir_texto(
                 negrito = True,
                 texto = 'Tecle U, I, O e P para controlar o jogo',
                 posicao_texto = (20, 380)
                 )

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    iniciar = botao(
        cor_botao = (0, 130, 0),
        posicao_tamanho = (100, 245, 200, 50),
        texto_botao = 'COMEÇAR',
        cor_mensagem = (255, 255, 255),
        posicao_texto = (150, 260)
        )
    tela_dificudade_ativa = botao(
        cor_botao = (130, 0, 0),
        posicao_tamanho = (100, 305, 200, 50),
        texto_botao = 'DIFICULDADE',
        cor_mensagem = (255, 255, 255),
        posicao_texto = (135, 320)
        )
    while tela_dificudade_ativa:
        relogio.tick(30)

        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

        tela_dificuldade()
        pygame.display.update()

    pygame.display.update()

    while iniciar:
        relogio.tick(30)
        tela.fill((cor_tela))

        for i in range (1, 10):
            grade = pygame.draw.line(tela, (57, 37, 67), (40 * i -1, 0), (40 * i -1, 600), 2)
        for i in range (1, 15):
            grade = pygame.draw.line(tela, (57, 37, 67), (0, 40 * i -1), (480, 40 * i -1), 2)

        exibir_texto(
            tamanho_fonte = 25,
            negrito = True,
            cor_texto = (0, 255, 0),
            texto = f'Pontos: {pontos}',
            posicao_texto = (10, 10)
        )
        exibir_texto(
            tamanho_fonte = 25,
            negrito=True,
            cor_texto = (255, 0, 0),
            texto = f'Erros: {erros}',
            posicao_texto = (300, 10)
        )
        if botao(
            cor_botao = (215, 87, 0),
            posicao_tamanho = (160, 5 , 80, 30),
            texto_botao ='INÍCIO',
            posicao_texto = (177, 12),
            tamanho_texto = 15
        ):
            iniciar = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN and (event.key == K_d or event.key == K_o):
                if x_personagem < 360:
                    x_personagem += 40
            elif event.type == KEYDOWN and (event.key == K_s or event.key == K_i):
                if x_personagem > 0:
                    x_personagem -= 40
            elif event.type == KEYDOWN and (event.key == K_f or event.key == K_p):
                if x_personagem == 320:
                    x_personagem += 40
                elif x_personagem < 320:
                    x_personagem += 80
            elif event.type == KEYDOWN and (event.key == K_a or event.key == K_u):
                if x_personagem == 40:
                    x_personagem -= 40
                elif x_personagem > 40:
                    x_personagem -= 80

        personagem_sombra = pygame.draw.rect(tela, (0, 0, 255), (x_personagem, 560, 40, 40))
        personagem = pygame.draw.rect(tela, (0, 0, 175), (x_personagem + 5, 565, 30, 30))
        comida_sombra = pygame.draw.rect(tela, cores_comida[cor], (x_comida, y_comida, 40, 40))
        comida = pygame.draw.rect(tela, cores_sombra_comida[cor], (x_comida + 5, y_comida +5, 30, 30))

        if personagem.colliderect(comida):
            x_comida = (randint(0, 9)) * 40
            y_comida = 0
            pontos += 1
            level_pontos += 1
            cor = randint(0, 6)
            if level_pontos == 10:
                level_pontos = 0
                velocidade += aumento_velocidade

        if y_comida <= altura:
            y_comida += velocidade
        else:
            erros += 1
            x_comida = (randint(0, 9)) * 40
            y_comida = 0
            cor = randint(0, 6)

        if erros == 5:
            perdeu = True
            while perdeu:
                tela.fill((cor_tela))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                if botao(
                    cor_botao = (0, 130, 0),
                    posicao_tamanho = (100, 245, 200, 50),
                    texto_botao = 'RECOMEÇAR',
                    cor_mensagem = (255, 255, 255),
                    posicao_texto = (135, 260)
                    ) == True:
                    reiniciar()
                if botao(
                    cor_botao = (150, 75, 0),
                    posicao_tamanho = (100, 305, 200, 50),
                    texto_botao = 'INÍCIO',
                    cor_mensagem = (255, 255, 255),
                    posicao_texto = (172, 320)
                    ) == True:
                    tela_inicio()
                exibir_texto(
                    tamanho_fonte = 25,
                    negrito = True,
                    texto = 'Você perdeu!',
                    cor_texto = (255, 0, 0),
                    posicao_texto = (100, 150)
                )
                exibir_texto(
                    tamanho_fonte = 25,
                    negrito = True,
                    texto = f'Sua pontuação: {pontos}',
                    cor_texto = (0, 255, 0),
                    posicao_texto = (100, 190)
                )
                pygame.display.update()
        pygame.display.update()
