# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 15:28:44 2022

@author: Thiago
"""

# =============================================================================
# ===================== MazeGame =============================
# 1. O jogador deve atravessar o labirinto sem atingir as paredes
# 2. O jogador pode se mover para cima, baixo, direita e esquerda
# 3. O jogador não pode sair nem bater nas bordas da tela, exceto na saída do
# labirinto
# 4. O jogo reinicia quando o jogador atinge as paredes (volta para posição inicial) 
# 5. O jogador ganha quando atinge a bolinha vermelha
# 6. O jogador é o cursor
# =============================================================================

# Imports
import sys, pygame
        
# Constantes da janela
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Inicializa o jogo
pygame.init()
 
# Cria a tela
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Cria o plano de fundo (não escalável, mas dava pra escalar)
fundo = pygame.image.load("fundo.png")

# Fonte para as mensagens
font = pygame.font.Font(None, 80)

# =============================================================================
# Cria as paredes do labirinto
# path é uma lista com tuples que irão definir coordenada e tamanho do retângulo ((x,y),(width, height))
# =============================================================================
path = [((0, 2.75), (471, 30)), ((441, 27), (30, 383)), ((231, 40), (269, 30)),
        ((243, 27), (30, 310)), ((206, 40), (30, 133)), ((147, 27), (30, 150)), 
        ((67, 27), (30, 445)), ((0, 100), (500, 30)), 
        ((10, 172), (167, 30)), ((206, 168), (162, 30)), ((363, 168), (30, 169)),
        ((10, 195), (30, 277)), ((92, 230), (408, 30)), ((480, 255), (30, 80)),
        ((0, 330), (500, 30)), ((135, 366), (250, 30)), ((110, 366), (30, 106)),
        ((10, 467), (130, 30)), ((380, 366), (30, 134)), ((157, 404), (314, 30)),
        ((157, 429), (30, 46)), ((182, 445), (183, 30)), ((335, 470), (30, 25)), 
        ((405, 470), (96, 30))]

# Coloca o mouse na posição inicial
pygame.mouse.set_pos(27, 10)

#Limita os frames do jogo
clock = pygame.time.Clock()

# Roda até o jogo acabar
running = True
while running:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
# =============================================================================
#     Condição para caso o mouse esteja dentro ou fora do caminho
#     -> O vetor b[][] irá percorrer a lista path em x AND y, verificando se o mouse está dentro ou fora
#     -> b[0] escolhe (x,y) e b[0][0] escolhe x (mesma ideia pra y)
#     -> b[1] escolhe (width, height) e b[1][0] escolhe width (mesma ideia pra height)
# =============================================================================
    if any(b[0][0] < pygame.mouse.get_pos()[0] < b[1][0] + b[0][0] and b[0][1] < pygame.mouse.get_pos()[1] < b[1][1] + b[0][1] for b in path):
        pass
    else:
        pygame.mouse.set_pos(27, 10)
    
    # Adiciona o fundo na tela
    screen.blit(fundo, (0,0))
        
    # Adiciona o caminho de acordo com o path
    for x in path:
        pygame.draw.rect(screen, "white", x)
    
    # Se o jogador chegar na bolinha vermelha ele ganha
    if( 339 < pygame.mouse.get_pos()[0] < 361 and 474 < pygame.mouse.get_pos()[1] < 495):
        vitoria = font.render("Vitória!", 1, "yellow")
        screen.blit(vitoria, (150, 200))
    
    # Cria o objetivo
    pygame.draw.circle(screen, "red", (350, 483), 10)
    
    # Atualiza o display conforme os eventos acontecem
    pygame.display.update()