import pygame

class Ladrillo():
    def __init__(self, ancho, alto):
        self.tablero = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.ancho=ancho
        self.alto = alto
        if self.tablero[alto][ancho] != 0:
            if self.tablero[alto][ancho] == 4:
                self.color = (255, 0, 255)
            elif self.tablero[alto][ancho] == 3:
                self.color = (0, 0, 255)
            elif self.tablero[alto][ancho] == 2:
                self.color = (100, 100, 100)
            elif self.tablero[alto][ancho] == 1:
                self.color = (255, 100, 0)



