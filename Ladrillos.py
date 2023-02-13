class Ladrillo():
    def __init__(self, x, y, puntos):
        super().__init__()

        self.__image = pygame.image.load('SOL.png')
        self.__rect = self.image.get_rect(x = x, y = y)
        self.__puntos = puntos

