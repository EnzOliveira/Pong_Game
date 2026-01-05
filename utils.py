# utils.py

# Não precisa de importações se as classes P1, P2 e Bola forem passadas como argumentos

def colisao_bola_jogador(j1, j2):
    # j1 e j2 são objetos de classes como P1/P2/Bola
    return (
        j1.x < j2.x + j2.largura and
        j1.x + j1.largura > j2.x and
        j1.y < j2.y + j2.altura and
        j1.y + j1.altura > j2.y
    )