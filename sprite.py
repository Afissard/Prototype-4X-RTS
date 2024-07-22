import pygame

class Sprite():
    def __init__(self, x, y, img_path) -> None:
        self.x = x
        self.y = y
        self.img = pygame.image.load(img_path).convert_alpha()
        self.rect = self.img.get_rect()

    def display(self, screen):
        screen.blit(self.img, (self.x, self.y))
