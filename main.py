import pygame
import sys

from src.player import Player
from src.world import World

# Inicialização
pygame.init()

# Configurações
LARGURA = 800
ALTURA = 600
FPS = 60

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("A Última Chama")

relogio = pygame.time.Clock()

# Cores
FUNDO = (25, 35, 45)
BRANCO = (255, 255, 255)
DOURADO = (255, 190, 70)
CINZA = (70, 80, 90)

# Fontes
fonte_titulo = pygame.font.Font(None, 80)
fonte_menu = pygame.font.Font(None, 42)
fonte_texto = pygame.font.Font(None, 30)

# Estados do jogo
estado = "menu"

# Inicialização do mundo e personagem
mundo = World()
jogador = Player(100, 100)


def desenhar_texto(texto, fonte, cor, x, y):
    imagem = fonte.render(texto, True, cor)
    retangulo = imagem.get_rect(center=(x, y))
    tela.blit(imagem, retangulo)


def desenhar_botao(texto, x, y, largura, altura):
    retangulo = pygame.Rect(x, y, largura, altura)

    mouse = pygame.mouse.get_pos()
    selecionado = retangulo.collidepoint(mouse)

    cor = DOURADO if selecionado else CINZA

    pygame.draw.rect(tela, cor, retangulo)

    desenhar_texto(
        texto,
        fonte_menu,
        BRANCO,
        retangulo.centerx,
        retangulo.centery
    )

    return retangulo


# Loop principal
executando = True

while executando:

    relogio.tick(FPS)

    tela.fill(FUNDO)

    # MENU PRINCIPAL
    if estado == "menu":

        desenhar_texto(
            "A ULTIMA CHAMA",
            fonte_titulo,
            DOURADO,
            400,
            130
        )

        botao_jogar = desenhar_botao(
            "NOVO JOGO", 280, 250, 240, 60
        )

        botao_como_jogar = desenhar_botao(
            "COMO JOGAR", 280, 330, 240, 60
        )

        botao_sair = desenhar_botao(
            "SAIR", 280, 410, 240, 60
        )

    # TELA DO JOGO
    elif estado == "jogo":

        teclas = pygame.key.get_pressed()

        jogador.atualizar(teclas, mundo.obstaculos)

        mundo.desenhar(tela)
        jogador.desenhar(tela)

        desenhar_texto(
            "ESC - Voltar ao menu",
            fonte_texto,
            DOURADO,
            400,
            30
        )

    # TELA DE INSTRUÇÕES
    elif estado == "instrucoes":

        desenhar_texto(
            "COMO JOGAR",
            fonte_titulo,
            DOURADO,
            400,
            150
        )

        desenhar_texto(
            "WASD - Movimentar",
            fonte_texto,
            BRANCO,
            400,
            260
        )

        desenhar_texto(
            "E - Interagir",
            fonte_texto,
            BRANCO,
            400,
            310
        )

        desenhar_texto(
            "ESC - Voltar",
            fonte_texto,
            BRANCO,
            400,
            360
        )

    # EVENTOS
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            executando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_ESCAPE:
                estado = "menu"

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if evento.button == 1 and estado == "menu":

                if botao_jogar.collidepoint(evento.pos):
                    estado = "jogo"

                elif botao_como_jogar.collidepoint(evento.pos):
                    estado = "instrucoes"

                elif botao_sair.collidepoint(evento.pos):
                    executando = False

    pygame.display.flip()

pygame.quit()
sys.exit()