import pygame 
import os
from settings import *


GRAVITY = False 

class Player(pygame.sprite.Sprite):
    def __init__(self, animation_images):
        pygame.sprite.Sprite.__init__(self)
        self.animation_images = animation_images
        self.image = pygame.image.load(self.animation_images['idle'][0])
        self.rect = self.image.get_rect() 
        self.state = "idle"
        self.animation_data = {
            "idle": self.load_images('idle'),
            "run": self.load_images('run'),
            "run_backwards": self.load_images('run_backwards'), # uses the 'run' images but will be flipped 
            "jump": self.load_images('jump'),
            "jumpdown": self.load_images('jumpdown'),
            "roll": self.load_images('roll'),
            "attack1": self.load_images('attack1'),
            "attack2": self.load_images('attack2'),
            "attack3": self.load_images('attack3'),
            "spattack": self.load_images('spattack'),
            "defend": self.load_images('defend'),
            "air_attack": self.load_images('air_attack'),
            "heal": self.load_images('heal')
            # will add more in main game 
        }
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
    
    def load_images(self, state):
        images = []
        for img in self.animation_images[state]:
            original_image = pygame.image.load(img).convert_alpha()
            larger_image = pygame.transform.scale(original_image, (original_image.get_width() * 3, original_image.get_height() * 3)) # Increase the size by 2 times
            images.append(larger_image)
        return images 
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += 5 # mo`ves the sprite right when "d" is pressed
            self.change_state('run')
        elif keys[pygame.K_n] and self.state != 'jump' and self.state != 'attack1' and self.state != 'attack2' and self.state != 'attack3':
            self.rect.x += 9 # performs roll when "n" is pressed 
            self.change_state('roll')
        elif keys[pygame.K_a]:
            self.rect.x -= 5 # moves the sprite left when "a" is pressed 
            self.change_state('run_backwards')            
        elif keys[pygame.K_SPACE] and self.state != 'attack1':
            self.rect.y -= 4 # moves sprite up when "space" is pressed
            self.change_state('jump')
        elif self.rect.y == 200:
            self.rect.y += 4
            self.change_state('jump')
        elif keys[pygame.K_LSHIFT] and self.state != 'attack1':
            self.rect.y += 4
            self.change_state('jumpdown')
        elif self.rect.y == 200:
            self.rect.y -= 4
            self.change_state('jumpdown')
        elif keys[pygame.K_b] and self.state != 'jump' and self.state != 'run':
            self.change_state('defend')
        elif keys[pygame.K_y] and self.state != 'run':
            self.change_state('attack1')
        elif keys[pygame.K_u] and self.state != 'run' and self.state != 'jump' and self.state != 'attack1':
            self.change_state('attack2')
        elif keys[pygame.K_i] and self.state != 'run' and self.state != 'jump' and self.state != 'attack1' and self.state != 'attack2':
            self.change_state('attack3')
        elif keys[pygame.K_o] and self.state != 'run' and self.state != 'jump' and self.state != 'attack1' and self.state != 'attack2' and self.state != 'roll':
            self.change_state('spattack')
        elif keys[pygame.K_SPACE] and keys[pygame.K_y] and self.state == 'jump':
            self.change_state('air_attack')
        elif keys[pygame.K_h]:
            self.change
        elif not keys[pygame.K_d] and self.state == 'run':
            self.change_state('idle')
        elif not keys[pygame.K_a] and self.state == 'run_backwards':
            self.change_state('idle')
        elif not keys[pygame.K_d] and self.state != 'run' and self.state != 'jump' and self.state != 'attack1' and self.state != 'attack2' and self.state != 'attack3' and self.state != 'spattack' and self.state != 'defend' and self.state != 'jumpdown':
            self.change_state('idle')
        self.animate() 
    
    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 80: #changes the speed of the animation by changiong the number 
            self.last_update = now
            self.current_frame = (self.current_frame + 1) %  len(self.animation_data[self.state])
            self.image = self.animation_data[self.state][self.current_frame]
            print(f"State: {self.state}, Frame: {self.current_frame}")
            if (self.state == 'jump' or self.state == 'jumpdown' or self.state == 'attack1' or self.state == 'attack2' or self.state =='attack3' or self.state == 'roll' or self.state == 'spattack' or self.state == 'defend') and self.current_frame == len(self.animation_data[self.state]) - 1:
                self.change_state('idle')
    
    def change_state(self, new_state):
         if new_state in self.animation_data and self.state != new_state:
            self.state = new_state
            self.current_frame = 0 # idle animation 

    
    def physics_engine(self, posx, posy):
        GRAVITY = True 
        pass 
        

def main_game(): 
    pygame.init() 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock() 

    animation_images = {
        'idle': [f'assets/sprites/brawler/spritesheets/01_idle/idle_{i}.png' for i in range (1, 8)],

        'run': [f'assets/sprites/brawler/spritesheets/02_run/run_{i}.png' for i in range (1, 8)],

        'run_backwards': [f'assets/sprites/brawler/spritesheets/02_run/run_{i}.png' for i in range (1, 8)],

        'jump': [f'assets/sprites/brawler/spritesheets/03_jump/jump_{i}.png' for i in range (1, 20)],

        'jumpdown': [f'assets/sprites/brawler/spritesheets/03_jump_down/jump_down_{i}.png' for i in range (1, 3)],

        'roll': [f'assets/sprites/brawler/spritesheets/04_roll/roll_{i}.png' for i in range (1, 8)],

        'attack1': [f'assets/sprites/brawler/spritesheets/05_1_atk/1_atk_{i}.png' for i in range (1, 11)],

        'attack2': [f'assets/sprites/brawler/spritesheets/06_2_atk/2_atk_{i}.png' for i in range (1, 18)],
        
        'attack3': [f'assets/sprites/brawler/spritesheets/07_3_atk/3_atk_{i}.png' for i in range (1, 28)],
        
        'spattack': [f'assets/sprites/brawler/spritesheets/08_sp_atk/sp_atk_{i}.png' for i in range (1, 18)],
        
        'defend': [f'assets/sprites/brawler/spritesheets/09_defend/defend_{i}.png' for i in range (1, 10)],

        'air_attack': [f'assets/sprites/brawler/spritesheets/air_atk/air_atk_{i}.png' for i in range (1, 8)],

        'heal': [f'assets/sprites/brawler/spritesheets/heal/frames/{i}.png' for i in range (0, 4)]
        
    }
    player = Player(animation_images)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    bg = pygame.image.load('zoomtest.png').convert_alpha()
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

    running = True 
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            
        all_sprites.update()
        screen.blit(bg, (0,0))
        all_sprites.draw(screen)
        pygame.display.flip() 
        
    pygame.quit()
    
if __name__ == '__main__':
    main_game() 
    