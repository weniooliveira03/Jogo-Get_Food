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
cores_comida = ((255, 0, 0), (255, 0, 127), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (127, 0, 255))
cores_sombra_comida = ((175, 0, 0), (175, 0, 87), (200, 87, 0), (175, 175, 0), (0, 175, 0), (0, 175, 175), (87, 0, 175))
cor = randint(0, 6)

pontos = 0
level_pontos = 0
erros = 0

tela = pygame.display.set_mode((largura, altura))
cor_tela = (50, 30, 60)
pygame.display.set_caption('Get Food')

fonte = pygame.font.SysFont('arial', 25, True, False)
fonte_inicio = pygame.font.SysFont('arial', 20, True, False)

relogio = pygame.time.Clock()

perdeu = False

iniciar = False


def botao(cor_botao, posicao_tamanho, texto_botao, cor_mensagem, posicao_mensagem):
    mouse = pygame.mouse.get_pos()

    exibir_sombra_botao = pygame.draw.rect(tela, (cor_botao[0] + 40, cor_botao[1] + 40, cor_botao[2] + 40), (posicao_tamanho))

    exibir_botao = pygame.draw.rect(tela, (cor_botao), (posicao_tamanho[0] + 5, posicao_tamanho[1] + 5, posicao_tamanho[2] - 10, posicao_tamanho[3] - 10))
    texto_botao = texto_botao

    exibir_texto_botao = fonte_inicio.render(texto_botao, True, (cor_mensagem), (cor_botao))
    tela.blit(exibir_texto_botao, (posicao_mensagem))

    if event.type == MOUSEBUTTONDOWN:
        if event.button == BUTTON_LEFT:
            if (posicao_tamanho[0] < mouse[0] < (posicao_tamanho[0] + posicao_tamanho[2])) and (posicao_tamanho[1] < mouse[1] < (posicao_tamanho[1] + posicao_tamanho[3])):
                return True
            

def reiniciar():
    global pontos, erros, perdeu, velocidade, level_pontos, iniciar
    pontos = 0
    erros = 0
    perdeu = False
    velocidade = 6
    level_pontos = 0

def tela_inicio():
    global iniciar

    iniciar = False
    reiniciar()

while True:
    tela.fill((cor_tela))

    m_inicio = f'Controle o jogo usando U, I, O e P'

    exibir_m_inicio = fonte_inicio.render(m_inicio, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    tela.blit(exibir_m_inicio, (35, 350))

    iniciar = botao(
        cor_botao = (0, 130, 0),
        posicao_tamanho = (100, 275, 200, 50),
        texto_botao = 'COMEÇAR',
        cor_mensagem = (255, 255, 255),
        posicao_mensagem = (150, 290)
        )

    pygame.display.update()

    while iniciar:
        relogio.tick(30)
        tela.fill((cor_tela))

        for i in range (1, 10):
            grade = pygame.draw.line(tela, (57, 37, 67), (40 * i -1, 0), (40 * i -1, 600), 2)
        for i in range (1, 15):
            grade = pygame.draw.line(tela, (57, 37, 67), (0, 40 * i -1), (480, 40 * i -1), 2)

        m_pontos = f'Pontuação: {pontos}'
        m_erros = f'Erros: {erros}'
        m_final1 = f'Você Perdeu!'
        m_final2 = f'Sua pontuação: {pontos}'
        m_final3 = f'Para recomeçar tecle espaço'

        exibir_pontos = fonte.render(m_pontos, True, (0, 255, 0))
        exibir_erros = fonte.render(m_erros, True, (255, 0, 0))
        exibir_m_final1 = fonte.render(m_final1, True, (255, 0, 0))
        exibir_m_final2 = fonte.render(m_final2, True, (0, 255, 0))
        exibir_m_final3 = fonte.render(m_final3, True, (0, 255, 255))

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

        destroy_sombra = pygame.draw.rect(tela, (0, 0, 175), (x_personagem, 560, 40, 40))
        destroy = pygame.draw.rect(tela, (0, 0, 255), (x_personagem + 5, 565, 30, 30))
        comida_sombra = pygame.draw.rect(tela, cores_comida[cor], (x_comida, y_comida, 40, 40))
        comida = pygame.draw.rect(tela, cores_sombra_comida[cor], (x_comida + 5, y_comida +5, 30, 30))

        if destroy.colliderect(comida):
            x_comida = (randint(0, 9)) * 40
            y_comida = 0
            pontos += 1
            level_pontos += 1
            cor = randint(0, 6)
            if level_pontos == 10:
                level_pontos = 0
                velocidade += 2

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
                    posicao_tamanho = (100, 240, 200, 50),
                    texto_botao = 'RECOMEÇAR',
                    cor_mensagem = (255, 255, 255),
                    posicao_mensagem = (135, 255)
                    ) == True:
                    reiniciar()
                if botao(
                    cor_botao = (150, 75, 0),
                    posicao_tamanho = (100, 310, 200, 50),
                    texto_botao = 'INÍCIO',
                    cor_mensagem = (255, 255, 255),
                    posicao_mensagem = (173, 325)
                    ) == True:
                    tela_inicio()

                tela.blit(exibir_m_final1, (100, 150))
                tela.blit(exibir_m_final2, (100, 190))

                pygame.display.update()

        tela.blit(exibir_pontos, (10, 10))
        tela.blit(exibir_erros, (300, 10))
        pygame.display.update()
