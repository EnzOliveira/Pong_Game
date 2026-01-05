# settings.py

# Importação de Pygame para constantes (opcional, mas útil)
import random

# --- CONSTANTES DE TELA ---
LARGURA_TELA = 800
ALTURA_TELA = 600

# --- CORES (RGB) ---
BRANCO = (255, 255, 255)
COR_P1 = BRANCO
COR_P2 = BRANCO
COR_BOLA = BRANCO

# --- ESTADOS DO JOGO ---
ESTADO_INICIAL = 0
ESTADO_JOGANDO = 1
SUBESTADO_POS_PONTO = 1.1
ESTADO_VITORIA = 2
ESTADO_PAUSE = 3

# --- CAMINHOS (Paths) ---
FUNDO_PATH = r"Pong\assets\img\Fundo Pong_800X600.jpg"
FONTE_PATH = r"Pong\assets\fonts\Geo-Regular.ttf"
SFX_COLISAO_PATH = r"Pong\assets\sounds\colision.wav"
SFX_PONTUACAO_PATH = r"Pong\assets\sounds\score.wav"
SFX_PONTUACAO_FINAL_PATH = r"Pong\assets\sounds\final_score.wav"

# --- CONFIGURAÇÕES DE JOGO/OBJETOS ---
LARGURA_JOGADORES = 8
ALTURA_JOGADORES = 50
VELOCIDADE_JOGADORES = 5
X_INICIAL_P1 = 20
Y_INICIAL_P1 = 250
X_INICIAL_P2 = LARGURA_TELA - 28
Y_INICIAL_P2 = 250


VELOCIDADE_BOLA_X = 4.9
VELOCIDADE_BOLA_Y = 4.9
ALTURA_BOLA = 10
LARGURA_BOLA = 10
X_INICIAL_BOLA = 396
Y_INICIAL_BOLA = random.randint(10, 500) # inicio de Y aleatório

PONTUACAO_PARA_VENCER = 11

FPS = 60
INTERVALO_PISCAR = 30