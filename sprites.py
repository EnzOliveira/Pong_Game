# sprites.py

import pygame
from settings import * # Importa todas as constantes que você precisa


# === CLASSES ===

# Classe do P1
class P1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = VELOCIDADE_JOGADORES
        self.altura = ALTURA_JOGADORES
        self.largura = LARGURA_JOGADORES
        # posições INICIAIS
        self.x_inicial = X_INICIAL_P1
        self.y_inicial = Y_INICIAL_P1
        

    def mover(self, teclas):
        if teclas[pygame.K_w]:
            self.y -= self.vel
        if teclas[pygame.K_s]:
            self.y += self.vel

        # setando limite vertical e horizontal
        self.x = max(0, min(self.x, LARGURA_TELA - self.altura))
        self.y = max(0, min(self.y, ALTURA_TELA - self.altura))
    
    def reset(self):
        self.x = self.x_inicial
        self.y = self.y_inicial

    def desenhar(self, tela):
        pygame.draw.rect(tela, COR_P1, (self.x, self.y, LARGURA_JOGADORES, ALTURA_JOGADORES))

# Classe do P2
class P2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = VELOCIDADE_JOGADORES
        self.altura = ALTURA_JOGADORES
        self.largura = LARGURA_JOGADORES
        # posições INICIAIS
        self.x_inicial = X_INICIAL_P2
        self.y_inicial = Y_INICIAL_P2

    def mover(self, teclas):
        if teclas[pygame.K_UP]:
            self.y -= self.vel
        if teclas[pygame.K_DOWN]:
            self.y += self.vel

        # setando limite vertical
        self.x = max(0, min(self.x, LARGURA_TELA - self.altura))
        self.y = max(0, min(self.y, ALTURA_TELA - self.altura))

    def reset(self):
        self.x = self.x_inicial
        self.y = self.y_inicial

    def desenhar(self, tela):
        pygame.draw.rect(tela, COR_P2, (self.x, self.y, LARGURA_JOGADORES, ALTURA_JOGADORES))

# Classe da Bola
class Bola:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = VELOCIDADE_BOLA_X
        self.vy = VELOCIDADE_BOLA_Y
        self.altura = ALTURA_BOLA
        self.largura = LARGURA_BOLA
        # posições
        self.x_inicial = X_INICIAL_BOLA
        self.y_inicial = Y_INICIAL_BOLA
        
    def colisao_tela(self):
        self.x += self.vx
        self.y += self.vy
        
        # Colisão com bordas
        
        if self.y <= 0 or self.y + self.altura >= ALTURA_TELA:
            self.vy *= -1  # inverte direção
        
    def verificar_ponto(self):
        if self.x <= 0:
            return 'p1'
        
        if self.x + self.largura >= LARGURA_TELA:
            return 'p2'

    def reset(self):
        self.x = self.x_inicial
        self.y = self.y_inicial

    def reset_apos_ponto(self, resultado, p1, p2):
        if resultado == 'p1':
            self.vx *= 1
            self.x = p1.x + 20
            self.y = p1.y + 25
        elif resultado == 'p2':
            self.vx *= -1
            self.x = p2.x - 20
            self.y = p2.y + 25

    def desenhar(self, tela):
        pygame.draw.rect(tela, COR_BOLA, (self.x, self.y, self.largura, self.altura))
