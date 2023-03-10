texto = fuente
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
import pygame

# Inicialización de Pygame
pygame.init()
# Inicialización de la superficie de dibujo
ventana = pygame. display.set_mode((640, 480))
pygame.display.set_caption('Ejemplo 1')

#Icono
pygame.display.set_caption("Icono")
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
speed = [5,5]
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

    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        barrarect = barrarect.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        barrarect = barrarect.move(5, 0)

    # Compruebo si hay colisión
    if barrarect.colliderect(ballrect):
        speed[1] = -speed[1]

    # Muevo la pelota
    ballrect = ballrect.move(speed)
    # Compruebo si la pelota llega a los límites de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]

    # Se pinta la ventana con un color
    # Esto borra los posibles elementos que teníamos anteriormente
    ventana.fill((0, 0, 0))

    # Dibujo la pelota
    ventana.blit(imag_redimensionada, ballrect)
    # Dibujo el bate
    ventana.blit(barra, barrarect)
    # Todos los elementos del juego se vuelven a dibujar
    pygame.display.flip()
    # Controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(60)

pygame.quit()

#Creación de Ladrillos
listas_sprites = pygame.sprite.Group()
bloques = pygame.sprite.Group()
for i in range(7):
    ladrillo = Ladrillo((255,255,0), 80, 30)
    ladrillo.rect.x = 60 * i * 100
    ladrillo.rect.y = 60
    listas_sprites.add(ladrillo)
    bloques.add(ladrillo)
for i in range(7):
    ladrillo = Ladrillo((255,255,0), 80, 30)
    ladrillo.rect.x = 60 * i * 100
    ladrillo.rect.y = 100
    listas_sprites.add(ladrillo)
    bloques.add(ladrillo)
for i in range(7):
    ladrillo = Ladrillo((255,255,0), 80, 30)
    ladrillo.rect.x = 60 * i * 100
    ladrillo.rect.y = 140
    listas_sprites.add(ladrillo)
    bloques.add(ladrillo)

    #Dibujo el bloque
    ventana.blit(bloques, listas_sprites)

 if imag_redimensionada.get_height() < 3*10+35+9:
        for altura in range(4):
            for anchura in range(10):
                if tablero.tablero[altura][anchura] != 0:
                    if ((anchura * 60 < imag_redimensionada.get_width() < anchura*60 + 59)
                           or (anchura*60 < imag_redimensionada.get_width() + 10 < anchura*60 +59)) and (
                            (altura*10 +35 < imag_redimensionada.get_height() < altura*10 + 35 + 9) or
                            (altura*10 +35 < imag_redimensionada.get_height()+10 < altura*10 + 35 + 9)):
                        tablero.tablero[altura][anchura] = 0
                        imag_redimensionada. *= -1