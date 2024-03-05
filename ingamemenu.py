import pygame 
import sys 
from settings import *


def draw_button(surface, x, y, width, height, text, text_colour, font, hover_colour=None):
    button_rect = pygame.Rect(x, y, width, height)

    # Check if the mouse is over the button
    is_hovered = button_rect.collidepoint(pygame.mouse.get_pos())

    # Draw the glowing outline when hovered or clicked
    if is_hovered:
        pygame.draw.rect(surface, (255, 255, 0), button_rect, border_radius=25, width=5)  # Yellow glowing outline

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


    


def pausemenu():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.init()

    pygame.display.set_caption('Pause Menu')
    clock = pygame.time.Clock()

    # create a semi-transparrent surface
    trans_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    # Fills the screen with the transparent value of 128
    trans_surface.fill((0, 0, 0, 128))
    font = pygame.font.Font(FONT1, 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button.collidepoint(event.pos):
                    print('Resume')
                elif options_button.collidepoint(event.pos):
                    print('Options Screen')
                elif reset_button.collidepoint(event.pos):
                    print('Options Screen')
                elif mainmenu_button.collidepoint(event.pos):
                    print('Options Screen')
                elif quitbutton_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit() 
        
        screen.blit(trans_surface, (0, 0))
        bar = pygame.image.load('assets/images/background/bar.png')
        screen.blit(bar,(50,50))

        resume_button = draw_button(screen, WIDTH - 1300, 100, 300, 100, "Resume", WHITE, font, hover_colour=GRAY)
        options_button = draw_button(screen, WIDTH - 1200, 250, 300, 100, "Options", WHITE, font, hover_colour=GRAY)
        reset_button = draw_button(screen, WIDTH - 1100, 400, 300, 100, "Reset", WHITE, font, hover_colour=GRAY)
        mainmenu_button = draw_button(screen, WIDTH - 1000, 550, 300, 100, "Main Menu", WHITE, font, hover_colour=GRAY)
        quitbutton_button = draw_button(screen, WIDTH - 900, 700, 300, 100, "Quit Game", WHITE, font, hover_colour=GRAY)

        

        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)

pausemenu()


