import pygame
from src.settings import VELOCIDADE
print("NOVO PLAYER.PY CARREGADO!")


class Player:
    def __init__(self, x, y):

        # Posição e colisão
        self.rect = pygame.Rect(x, y, 30, 20)
        self.velocidade = VELOCIDADE

        # Carrega a spritesheet
        self.spritesheet = pygame.image.load(
            "assets/sprites/player/player_sheet.png"
        ).convert_alpha()

        # Configuração dos quadros
        self.largura_frame = 256
        self.altura_frame = 256

        self.animacoes = {
            "baixo": [],
            "esquerda": [],
            "direita": [],
            "cima": []
        }

        direcoes = [
            "baixo",
            "esquerda",
            "direita",
            "cima"
        ]

        # Separa os quadros da spritesheet
        for linha, direcao in enumerate(direcoes):
            for coluna in range(3):

                frame = pygame.Surface(
                    (256, 256),
                    pygame.SRCALPHA
                )

                frame.blit(
                    self.spritesheet,
                    (0, 0),
                    (
                        coluna * 256,
                        linha * 256,
                        256,
                        256
                    )
                )

                # Redimensiona o personagem
                frame = pygame.transform.scale(
                    frame,
                    (48, 48)
                )

                self.animacoes[direcao].append(frame)

        self.direcao = "baixo"
        self.frame_atual = 0
        self.tempo_animacao = 0

    def atualizar(self, teclas, obstaculos):

        dx = 0
        dy = 0

        if teclas[pygame.K_w]:
            dy -= self.velocidade
            self.direcao = "cima"

        elif teclas[pygame.K_s]:
            dy += self.velocidade
            self.direcao = "baixo"

        if teclas[pygame.K_a]:
            dx -= self.velocidade
            self.direcao = "esquerda"

        elif teclas[pygame.K_d]:
            dx += self.velocidade
            self.direcao = "direita"

        movimento = pygame.Vector2(dx, dy)

        if movimento.length() > 0:

            movimento = movimento.normalize() * self.velocidade

            # Atualiza animação
            self.tempo_animacao += 1

            if self.tempo_animacao >= 10:
                self.frame_atual = (
                    self.frame_atual + 1
                ) % 3

                self.tempo_animacao = 0

        else:
            self.frame_atual = 0
            self.tempo_animacao = 0

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

        imagem = self.animacoes[
            self.direcao
        ][self.frame_atual]

        # Centraliza o sprite sobre a área de colisão
        posicao = imagem.get_rect(
            midbottom=self.rect.midbottom
        )

        tela.blit(imagem, posicao)