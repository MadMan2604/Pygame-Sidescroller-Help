import pygame 

# Class for the fighter button icon 
class FighterButton(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def draw(self, surface):
        surface.blit(self.image, self.rect)
