# game_manager.py

import pygame
import random
from settings import *
from sprites import P1, P2, Bola
from utils import colisao_bola_jogador

class GameManager:
    def __init__(self, tela):
        self.tela = tela
        self.fundo = pygame.image.load(FUNDO_PATH)
        self.estado_do_jogo = ESTADO_INICIAL
        self.p1 = P1(X_INICIAL_P1, Y_INICIAL_P1)
        self.p2 = P2(X_INICIAL_P2, Y_INICIAL_P2)
        self.bola = Bola(LARGURA_TELA // 2 - 5, ALTURA_TELA // 2 - 5)
        self.vencedor = None
        
        # Sons
        self.sfx_colisao = pygame.mixer.Sound(SFX_COLISAO_PATH)
        self.sfx_score = pygame.mixer.Sound(SFX_PONTUACAO_PATH)
        self.sfx_final_score = pygame.mixer.Sound(SFX_PONTUACAO_FINAL_PATH)

        # Placar
        self.resultado = None
        self.p1_score = 0
        self.p2_score = 0
        self.fonte = pygame.font.Font(FONTE_PATH, 100)
        
        # Piscar Pontuação Vencecdora
        self.contador_piscar = 0
        self.p1_pontuacao_visivel = True
        self.p2_pontuacao_visivel = True

    # Lógica para P, R, e ESC
    def funcoes_teclas(self, teclas):
        # "P" como tecla de pause e despause
        if teclas[pygame.K_p]:
            if self.estado_do_jogo == ESTADO_JOGANDO:
                self.estado_do_jogo = ESTADO_PAUSE
            else:
                self.estado_do_jogo = ESTADO_JOGANDO
        # ESC para sair do estado de pause
        if teclas[pygame.K_ESCAPE]:
            if self.estado_do_jogo == ESTADO_PAUSE:
                self.estado_do_jogo = ESTADO_JOGANDO

        if teclas[pygame.K_r]:
            self.estado_do_jogo = ESTADO_INICIAL
            self.p1_score = 0
            self.p2_score = 0
            self.p1_pontuacao_visivel = True
            self.p2_pontuacao_visivel = True
            self.bola.y_inicial = Y_INICIAL_BOLA

    def update_logic(self, teclas):
        # Atualiza o jogo dependendo do ESTADO
        if self.estado_do_jogo == ESTADO_JOGANDO:
            self.p1.mover(teclas)
            self.p2.mover(teclas)
            self.bola.colisao_tela()
            
            # Checar Colisões e Pontuação
            # colisão p1 -> bola
            if colisao_bola_jogador(self.p1, self.bola):
                self.bola.vx *= -1
                self.sfx_colisao.play()
            # colisão p2 -> bola
            if colisao_bola_jogador(self.p2, self.bola):
                self.bola.vx *= -1
                self.sfx_colisao.play()

            # verificar quem recebe o ponto
            self.resultado = self.bola.verificar_ponto()
            if self.resultado == 'p1':
                self.sfx_score.play()
                self.p1_score += 1
                self.bola.y_inicial = Y_INICIAL_BOLA
                self.bola.reset_apos_ponto(self.resultado, self.p1, self.p2)
                self.estado_do_jogo = SUBESTADO_POS_PONTO

            elif self.resultado == 'p2':
                self.sfx_score.play()
                self.p2_score += 1
                self.bola.y_inicial = Y_INICIAL_BOLA
                self.bola.reset_apos_ponto(self.resultado, self.p1, self.p2)
                self.estado_do_jogo = SUBESTADO_POS_PONTO

            # Verficando se há vencedor
            if self.p1_score == PONTUACAO_PARA_VENCER:
                self.estado_do_jogo = ESTADO_VITORIA
                self.vencedor = 'p1'
            if self.p2_score == PONTUACAO_PARA_VENCER:
                self.estado_do_jogo = ESTADO_VITORIA
                self.vencedor = 'p2'
        
        # Se em sub_estado de pós ponto mantem o jogo parado até ação 
        elif self.estado_do_jogo == SUBESTADO_POS_PONTO:
            self.bola.reset_apos_ponto(self.resultado, self.p1, self.p2)

            self.p1.mover(teclas)
            self.p2.mover(teclas)

            # Impede o inicio do jogo até uma das teclas ser pressionada
            if self.resultado == 'p1' and teclas[pygame.K_d]:
                self.estado_do_jogo = ESTADO_JOGANDO
            elif self.resultado == 'p2' and teclas[pygame.K_LEFT]:
                self.estado_do_jogo = ESTADO_JOGANDO

        # Se estado de jogo igual a ESTADO_INICIAL
        elif self.estado_do_jogo == ESTADO_INICIAL:
            self.bola.reset()
            self.p1.reset()
            self.p2.reset()

            # Impede o inicio do jogo até uma das teclas ser pressionada
            if teclas[pygame.K_w] or teclas[pygame.K_s] or teclas[pygame.K_UP] or teclas[pygame.K_DOWN] or teclas[pygame.K_SPACE]:
                self.estado_do_jogo = ESTADO_JOGANDO
        
        # Se estado de jogo igual a ESTADO_VITORIA
        elif self.estado_do_jogo == ESTADO_VITORIA:
            self.update_piscar_placar_vencedor() # Chama a função de piscar
            
    def update_piscar_placar_vencedor(self):
        # Lógica de piscar pontuação vencedora
        self.contador_piscar += 1
        if self.vencedor == 'p1' and self.contador_piscar >= INTERVALO_PISCAR:
            self.p1_pontuacao_visivel = not self.p1_pontuacao_visivel
            self.sfx_final_score.play()
            self.contador_piscar = 0

        if self.vencedor == 'p2' and self.contador_piscar >= INTERVALO_PISCAR:
            self.p2_pontuacao_visivel = not self.p2_pontuacao_visivel
            self.sfx_final_score.play()
            self.contador_piscar = 0

    def draw(self):
        # Lógica de Desenho
        self.tela.blit(self.fundo, (0, 0)) # Fundo deve ser carregado aqui ou em __init__
        self.p1.desenhar(self.tela)
        self.p2.desenhar(self.tela)
        self.bola.desenhar(self.tela)
        self.draw_score()

    def draw_score(self):
        p1_score_text = self.fonte.render(str(self.p1_score), True, BRANCO)
        p2_score_text = self.fonte.render(str(self.p2_score), True, BRANCO)

        # Usando as variáveis de visibilidade do placar
        if self.p1_pontuacao_visivel:
            self.tela.blit(p1_score_text, (450, 10))
        if self.p2_pontuacao_visivel:
            self.tela.blit(p2_score_text, (300, 10))