import pygame
import sys 
from settings import *
from pygame import mixer
from time import sleep  
from FighterButton import FighterButton
from level import Level 
from earthmonk import *
from chartest import *


#initialise pygame
pygame.init() 

entireword = []

#load window
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption(GAME_TITLE)

clock = pygame.time.Clock() 

# Font for the buttons 
font = pygame.font.Font("assets/fonts/DungeonFont.ttf", 200)
font1 = pygame.font.Font(None, 36)
font2 = pygame.font.Font("assets/fonts/DungeonFont.ttf", 55)

# load character icon
icon1 = pygame.image.load("assets/Sprites/brawler/fire_knight.png").convert_alpha()

# load spritesheets
warrior_sheet = pygame.image.load("assets/Sprites/monk/ground_monk.png").convert_alpha()


def draw_button(surface, colour, x, y, width, height, text, text_colour, font, hover_colour=None):
    button_rect = pygame.Rect(x, y, width, height)

    # Check if the mouse is over the button
    is_hovered = button_rect.collidepoint(pygame.mouse.get_pos())

    # Draw the rectangular part of the button
    pygame.draw.rect(surface, colour, button_rect, border_radius=25)

    # Draw the semicircles on each end
    left_semicycle_rect = pygame.Rect(x, y, height, height)
    right_semicycle_rect = pygame.Rect(x + width - height, y, height, height)

    pygame.draw.ellipse(surface, colour, left_semicycle_rect)
    pygame.draw.ellipse(surface, colour, right_semicycle_rect)

    # Draw the glowing outline when hovered or clicked
    if is_hovered:
        pygame.draw.rect(surface, (255, 255, 0), button_rect, border_radius=25, width=5)  # Yellow glowing outline
    else:
        pygame.draw.rect(surface, (255, 255, 255), button_rect, border_radius=25, width=5)  # White outline

    button_text = font.render(text, True, text_colour)

    # Adjust font size based on the hover state
    if is_hovered:
        font_size = 40  # Increased font size when hovered
    else:
        font_size = 36

    button_text = pygame.font.Font.render(font, text, True, text_colour)
    button_text = pygame.transform.scale(button_text, (width, height))

    # Center the text on the button
    text_rect = button_text.get_rect(center=button_rect.center)

    surface.blit(button_text, text_rect.topleft)

    return button_rect


# Initialise Title Screen
def title_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is on the "Play" button
                if play_button.collidepoint(event.pos):
                    # Add code here to change game state
                    dialogue_screen()
                # Check if the mouse click is on the "Quit" button
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # Draw the title and buttons
        # tmbg = title menu background
        tmbg = pygame.image.load("assets/images/background/tmbg.png").convert_alpha()
        tmbg = pygame.transform.scale(tmbg, (WIDTH, HEIGHT))
        screen.blit(tmbg, (0, 0))
        title_text = font.render("Archans Echos", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))

        # Draw play button
        play_button = draw_button(screen, WHITE, WIDTH // 2 - 150, 500, 300, 50, "Play", BLACK, font1, hover_colour=GRAY)

        # Draw quit button
        quit_button = draw_button(screen, WHITE, WIDTH // 2 - 150, 700, 300, 50, "Quit", BLACK, font1, hover_colour=GRAY)

        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)

# Initialise Game Info Screen 
def dialogue_screen():
    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click on "ENTER"
                if enter_button.collidepoint(event.pos):
                    # Add code here to enter game 
                    charselect_screen()
                # Check if the mouse click on "Back"
                if back_button.collidepoint(event.pos):
                    title_screen()

        # Draw the dialogue
        # dmbg = dialogue menu background
        dmbg = pygame.image.load("assets/images/background/dmbg.png").convert_alpha()
        dmbg = pygame.transform.scale(dmbg, (WIDTH, HEIGHT))
        screen.blit(dmbg, (0, 0))
        dialogue_text = font2.render("The aim of the game is to beat the boss at the end, if you die, the game resets", True, BLACK)
        screen.blit(dialogue_text, (WIDTH // 2 - dialogue_text.get_width() // 2, 100))
        

        # Draw play button 
        enter_button = draw_button(screen, WHITE, WIDTH // 2 - 100, 500, 200, 50, "Enter", BLACK, font1, hover_colour=GRAY)

        # Draw quit button 
        back_button = draw_button(screen, WHITE, WIDTH // 2 - 100, 700, 200, 50, "Back", BLACK, font1, hover_colour=GRAY)

        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)

 

# Initialise Character Selection Screen 
def charselect_screen():
    # Load character icons
    warrior_icon = pygame.image.load('assets/icons/fire_knight.png').convert()
    knight_icon = pygame.image.load('assets/Sprites/monk/ground_monk.png').convert()
    warrior_icon = pygame.transform.scale(warrior_icon, (warrior_icon.get_width() * 3, warrior_icon.get_height() * 3))
    knight_icon = pygame.transform.scale(knight_icon, (knight_icon.get_width() * 3, knight_icon.get_height() * 3))

    # Create buttons for each character
    warrior_button = FighterButton(warrior_icon, (500, 450))
    knight_button = FighterButton(knight_icon, (1000, 450))

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if warrior_button.rect.collidepoint(event.pos):
                    main_game()
                    # Add code here to set the player's character to the warrior
                elif knight_button.rect.collidepoint(event.pos):
                    main() 
                    # Add code here to set the player's character to the mage
                elif backbutton.collidepoint(event.pos):
                    dialogue_screen()
    
        # Draw background
        csbg = pygame.image.load("assets/images/background/csbg.png")
        csbg = pygame.transform.scale(csbg, (WIDTH, HEIGHT))
        screen.blit(csbg, (0, 0))

        # Draw character buttons
        warrior_button.draw(screen)
        knight_button.draw(screen)

        # Draw back button 
        backbutton = draw_button(screen, WHITE, WIDTH // 2 - 600, 900, 200, 50, "Back", BLACK, font1, hover_colour=GRAY)

        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)


# Call the title screen function
title_screen()   

# Initialise the Main Game Loop
## The game loop has to load the main game levels + the character animations 
def main_game():
    # Define the sound mechanics 
    main_sound = pygame.mixer.Sound('assets/audio/main.mp3')
    main_sound.set_volume(0.3)
    
    level = Level()


    while True: 
        for event in pygame.event.get:
            if event.type == pygame.QUIT():
                pygame.quit()
                sys.exit()

        # load the sound for the main game 
               
        main_sound.play(loops = -1)

        # Run level 
        level.run()

            
        # Draw Background 
        main_background = pygame.image.load("assets/images/background/background.png")
        main_background = pygame.transform.scale(main_background, (WIDTH, HEIGHT))
        screen.blit(main_background, (0, 0))

        # show player stats 

        # update fighters

        # call the enemy scripts here 
        



