import time

import pygame
from Ladrillos import Ladrillo

# Inicialización de Pygame
pygame.init()
# Inicialización de la superficie de dibujo
W,H = 640, 480
ventana = pygame. display.set_mode((W, H))
FPS = 60
reloj = pygame.time.Clock()
#Fondo del juego
fondo = pygame.image.load("Fondo.png").convert()
y = 0

#GAME OVER
fuente = pygame.font.Font(None, 150)
texto = fuente.render("Game Over", True, (125, 125, 125))
texto_rect = texto.get_rect()
texto_x = ventana.get_width() / 2 - texto_rect.width / 2
texto_y = ventana.get_height() / 2.5 - texto_rect.height / 2.5
#Como parar el juego una vez que salga el GAME OVER
fuente2 = pygame.font.Font(None, 50)
texto2 = fuente2.render("Pulsa ESPACIO para salir", True, (125,125,125))
texto2_rect = texto2.get_rect()
texto2_x = ventana.get_width() / 2 - texto2_rect.width / 2
texto2_y = ventana.get_height() / 1.5 - texto2_rect.height / 1.5

#Icono y Título
pygame.display.set_caption("Aritz & Andy's GAME")
icono = pygame.image.load("Icono.png")
pygame.display.set_icon(icono)

# Crea el objeto pelota y la redimensiono
ball = pygame.image.load("SOL.png")
ancho = 40
alto = 40
imag_redimensionada = pygame.transform.scale(ball, (ancho, alto))
# Obtengo el rectángulo del objeto anterior
ballrect = imag_redimensionada.get_rect()
# Inicializo los valores con los que se van a mover la pelota y su velocidad
speed = [1, -1]
ball_speed = 5
# Pongo la pelota en el origen de coordenadas
ballrect.move_ip(0,0)

# Crea el objeto bate, y obtengo su rectángulo
barra = pygame.image.load("LASER.png")
barrarect = barra.get_rect()
# Pongo el bate en la parte inferior de la pantalla
barrarect.move_ip(240, 450)

#Ladrillos
lista_tableros = []
for alto in range(4):
    for ancho in range(11):
            lista_tableros.append(Ladrillo(ancho, alto))

# Bucle principal del juego
jugando = True
while jugando:
    # Comprobamos los eventos
    # Comprobamos si se ha pulsado el botón de cierre de la ventana
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_SPACE]:
            jugando = False
    #Movimiento del fondo de pantalla
    y_relativa = y % fondo.get_rect().height
    ventana.blit(fondo, (0, y_relativa - fondo.get_rect().height))
    if y_relativa < H:
        ventana.blit(fondo, (0, y_relativa))
    y -= 1
    reloj.tick(FPS)

    # Compruebo si se ha pulsado alguna tecla y le marco los bordes de la pantalla:
    if keys[pygame.K_LEFT] and barrarect.left > 0:
        barrarect = barrarect.move(-10, 0)
    if keys[pygame.K_RIGHT] and barrarect.right < ventana.get_width():
        barrarect = barrarect.move(10, 0)

    # Compruebo si hay colisión y aumento gradualmente la velocidad
    if barrarect.colliderect(ballrect):
        speed[1] = -speed[1]
        if ball_speed < 15:
            ball_speed = ball_speed + 1

    # Muevo la pelota
    ballrect = ballrect.move(speed[0]*ball_speed, speed[1]*ball_speed)
    # Compruebo si la pelota llega a los límites de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]

    # Se pinta la ventana con un color
    # Esto borra los posibles elementos que teníamos anteriormente

    # Dibujo la pelota
    ventana.blit(imag_redimensionada, ballrect)
    # Dibujo el bate
    ventana.blit(barra, barrarect)
    # Dibujo ladrillo
    for tablero in lista_tableros:
        pygame.draw.rect(ventana, tablero.color, (tablero.ancho * 60, tablero.alto * 10 + 35, 59, 9))

    # Todos los elementos del juego se vuelven a dibujar
    if ballrect.bottom > ventana.get_height():
        ventana.blit(texto, [texto_x, texto_y])
        ventana.blit(texto2, [texto2_x, texto2_y])
    pygame.display.flip()
    # Controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(60)



pygame.quit()