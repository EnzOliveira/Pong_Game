# main.py

import pygame
from settings import LARGURA_TELA, ALTURA_TELA, FUNDO_PATH, FPS
from game_manager import GameManager

# === INICIALIZAÇÃO PYGAME ===
pygame.init()

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Pong")

# Inicializa o Game Manager e o Clock
jogo = GameManager(tela)
clock = pygame.time.Clock()

# === LOOP PRINCIPAL ===
rodando = True
while rodando:
    teclas = pygame.key.get_pressed()

    # --- 1. EVENTOS ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        # verifica o pressionamento das teclas (que possuem funções fora movimentação)
        jogo.funcoes_teclas(teclas)
    # --- 2. ATUALIZAÇÃO DA LÓGICA ---
    jogo.update_logic(teclas)
    
    # --- 3. DESENHO ---
    jogo.draw()
    
    # --- 4. ATUALIZAÇÃO DA TELA ---
    pygame.display.flip()
    
    # Controla o FPS
    clock.tick(FPS) 

# === FINALIZAÇÃO ===
pygame.quit()