import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 400
altura = 600

x = 160

x_comida = (randint(0, 9)) * 40
y_comida = 0
velocidade = 6
cores = ((255, 0, 0), (255, 0, 127), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (127, 0, 255))
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
    global iniciar

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
    global pontos, erros, perdeu, velocidade, level_pontos
    pontos = 0
    erros = 0
    perdeu = False
    velocidade = 4
    level_pontos = 0


while True:
    tela.fill((cor_tela))

    m_inicio2 = f'Controle o jogo usando K e L'

    exibir_m_inicio2 = fonte_inicio.render(m_inicio2, True, (255, 255, 255))

    mouse = pygame.mouse.get_pos()   

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                iniciar = True

    tela.blit(exibir_m_inicio2, (40, 350))

    if botao(
        cor_botao = (0, 130, 0),
        posicao_tamanho = (100, 275, 200, 50),
        texto_botao = 'COMEÇAR',
        cor_mensagem = (255, 255, 255),
        posicao_mensagem = (150, 290)
        ) == True:
        iniciar = True

    pygame.display.update()

    while iniciar:
        relogio.tick(30)
        tela.fill((cor_tela))

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
            if event.type == KEYDOWN and x < 360:
                if event.key == K_RIGHT or event.key == K_l:
                    x += 40
            if event.type == KEYDOWN and x > 0:
                if event.key == K_LEFT or event.key == K_k:
                    x -= 40

        destroy = pygame.draw.rect(tela, (0, 0, 255), (x, 560, 40, 40))
        comida = pygame.draw.rect(tela, cores[cor], (x_comida, y_comida, 40, 40))

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
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            reiniciar()

                tela.blit(exibir_m_final1, (30, 230))
                tela.blit(exibir_m_final2, (30, 280))
                tela.blit(exibir_m_final3, (30, 330))

                pygame.display.update()

        tela.blit(exibir_pontos, (10, 10))
        tela.blit(exibir_erros, (300, 10))
        pygame.display.update()
