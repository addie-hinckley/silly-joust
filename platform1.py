
import pygame

class Platform1(pygame.sprite.Sprite):

    def __init__(self, location: tuple, size: tuple, color: str):

        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = location)




