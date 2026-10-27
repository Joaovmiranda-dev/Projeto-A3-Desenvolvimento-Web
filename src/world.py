import pygame
from src.settings import *

MAPA = [
    "####################",
    "#..................#",
    "#..................#",
    "#....####..........#",
    "#....####..........#",
    "#..................#",
    "#..........####....#",
    "#..........####....#",
    "#..................#",
    "#..................#",
    "#....####..........#",
    "#....####..........#",
    "#..................#",
    "#..................#",
    "####################",
]


class World:
    def __init__(self):
        self.obstaculos = []

        for linha, conteudo in enumerate(MAPA):
            for coluna, tile in enumerate(conteudo):
                if tile == "#":
                    rect = pygame.Rect(
                        coluna * TAMANHO_TILE,
                        linha * TAMANHO_TILE,
                        TAMANHO_TILE,
                        TAMANHO_TILE
                    )
                    self.obstaculos.append(rect)

    def desenhar(self, tela):
        tela.fill(VERDE)

        for linha, conteudo in enumerate(MAPA):
            for coluna, tile in enumerate(conteudo):
                x = coluna * TAMANHO_TILE
                y = linha * TAMANHO_TILE

                if tile == "#":
                    pygame.draw.rect(
                        tela,
                        VERDE_ESCURO,
                        (x, y, TAMANHO_TILE, TAMANHO_TILE)
                    )
                else:
                    pygame.draw.rect(
                        tela,
                        (95, 175, 85),
                        (x, y, TAMANHO_TILE, TAMANHO_TILE),
                        1
                    )