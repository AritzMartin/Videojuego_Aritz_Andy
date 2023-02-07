import pygame

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
# Inicializo los valores con los que se van a mover la pelota
speed = [1, -1]  
ball_speed = 5
# Pongo la pelota en el origen de coordenadas
ballrect.move_ip(0,0)

# Crea el objeto bate, y obtengo su rectángulo
barra = pygame.image.load("LASER.png")
barrarect = barra.get_rect()
# Pongo el bate en la parte inferior de la pantalla
barrarect.move_ip(240, 450)

# Bucle principal del juego
jugando = True
while jugando:
    # Comprobamos los eventos
    # Comprobamos si se ha pulsado el botón de cierre de la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    #Movimiento del fondo de pantalla
    y_relativa = y % fondo.get_rect().height
    ventana.blit(fondo, (0, y_relativa - fondo.get_rect().height))
    if y_relativa < H:
        ventana.blit(fondo, (0, y_relativa))
    y -= 1
    reloj.tick(FPS)

    # Compruebo si se ha pulsado alguna tecla y le marco los bordes de la pantalla:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and barrarect.left > 0:
        barrarect = barrarect.move(-10, 0)
    if keys[pygame.K_RIGHT] and barrarect.right < ventana.get_width():
        barrarect = barrarect.move(10, 0)


    # Compruebo si hay colisión
    if barrarect.colliderect(ballrect):
        speed[1] = -speed[1]
        if ball_speed < 15:
            ball_speed = ball_speed + 1

    # Muevo la pelota
    ballrect = ballrect.move(speed[0]*ball_speed, speed[1]*ball_speed)
    # Compruebo si la pelota llega a los límites de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]

    # Se pinta la ventana con un color
    # Esto borra los posibles elementos que teníamos anteriormente


    # Dibujo la pelota
    ventana.blit(imag_redimensionada, ballrect)
    # Dibujo el bate
    ventana.blit(barra, barrarect)
    # Todos los elementos del juego se vuelven a dibujar
    pygame.display.flip()
    # Controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(60)

pygame.quit()