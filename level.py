import pygame, sys 
import pytmx
from pytmx.util_pygame import load_pygame 
from settings import *
from camera import Camera
from character import Character
from fireknight import Player
import collections

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

pygame.init()
screen = pygame.display.set_mode((SWIDTH,SHEIGHT))
s_screen = pygame.surface.Surface((SWIDTH, SHEIGHT))
tmx_data = load_pygame('assets/Level1/level1.tmx')
sprite_group = pygame.sprite.Group()
clock = pygame.time.Clock()

# Iterate over all visible layers
for layer in tmx_data.visible_layers:
    # Check if the layer is a tile layer
    if isinstance(layer, pytmx.TiledTileLayer):
        # Iterate over all tiles in the layer
        for x, y, gid in layer:
            # Get the tile image
            tile_image = tmx_data.get_tile_image_by_gid(gid)
            # Create a Tile sprite for the tile
            if tile_image is not None:
                Tile((x * tmx_data.tilewidth, y * tmx_data.tileheight), tile_image, sprite_group)

# Create a Camera
camera = Camera(tmx_data.width * tmx_data.tilewidth, tmx_data.height * tmx_data.tileheight)
character = Player()
sprite_group.add(character)

fps_log = collections.deque(maxlen=20)

while True:

    clock.tick(FPS * 2)
    fps_log.append(clock.get_fps())
    fps = sum(fps_log) / len(fps_log)
    
    

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the Character
    character.update()
    # Update the Camera 
    camera.update(character)

    screen.fill(BLACK)
    
    # Draw all tiles
    for sprite in sprite_group:
        rect, image = camera.apply(sprite)
        s_screen.blit(image, rect)
    
    screen.blit(s_screen, (0, 0))
    
    pygame.display.update()
    pygame.display.flip()
