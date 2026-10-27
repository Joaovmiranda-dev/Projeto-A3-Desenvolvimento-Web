import pygame
from src.settings import VELOCIDADE, AZUL


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.velocidade = VELOCIDADE

    def atualizar(self, teclas, obstaculos):
        dx = 0
        dy = 0

        if teclas[pygame.K_w]:
            dy -= self.velocidade
        if teclas[pygame.K_s]:
            dy += self.velocidade
        if teclas[pygame.K_a]:
            dx -= self.velocidade
        if teclas[pygame.K_d]:
            dx += self.velocidade

        # Impede movimento diagonal mais rápido
        movimento = pygame.Vector2(dx, dy)

        if movimento.length() > 0:
            movimento = movimento.normalize() * self.velocidade

        # Colisão horizontal
        self.rect.x += round(movimento.x)

        for obstaculo in obstaculos:
            if self.rect.colliderect(obstaculo):
                if movimento.x > 0:
                    self.rect.right = obstaculo.left
                elif movimento.x < 0:
                    self.rect.left = obstaculo.right

        # Colisão vertical
        self.rect.y += round(movimento.y)

        for obstaculo in obstaculos:
            if self.rect.colliderect(obstaculo):
                if movimento.y > 0:
                    self.rect.bottom = obstaculo.top
                elif movimento.y < 0:
                    self.rect.top = obstaculo.bottom

    def desenhar(self, tela):
        pygame.draw.rect(tela, AZUL, self.rect)