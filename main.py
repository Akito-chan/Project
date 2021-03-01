import pygame
import sys
from pygame.locals import *
import os
import random
from level_1 import level
# Game Initialization

class Main_menu:
    def __init__(self):

        pygame.init()

        WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600


        # Center the Game Application
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        # Game Resolution
        screen_width = 800
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))

        # Text Renderer
        def text_format(message, textFont, textSize, textColor):
            newFont = pygame.font.Font(textFont, textSize)
            newText = newFont.render(message, 0, textColor)

            return newText


        # Colors
        white = (255, 255, 255)
        black = (0, 0, 0)
        gray = (50, 50, 50)
        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
        yellow = (255, 255, 0)

        # Game Fonts
        font = "FaunaOne-Regular.ttf"
        font1 = "CinzelDecorative-Black.ttf"


        # Game Framerate
        clock = pygame.time.Clock()
        FPS = 30

        def terminate():
            pygame.quit()
            sys.exit
    
        def main_menu():

            menu=True
            selected="start"

            while menu:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            selected="start"
                        elif event.key == pygame.K_DOWN:
                            selected="quit"
                        if event.key == pygame.K_RETURN:
                            if selected == "start":
                                level()
                            if selected == "quit":
                                terminate()
                                break

                # Main Menu UI
                screen.fill(blue)
                title = text_format("IN WONDERLAND", font1, 70, yellow)
                if selected == "start":
                    text_start = text_format("START", font, 55, white)
                else:
                    text_start = text_format("START", font, 55, black)
                if selected == "quit":
                    text_quit = text_format("QUIT", font, 55, white)
                else:
                    text_quit = text_format("QUIT", font, 55, black)

                title_rect = title.get_rect()
                start_rect = text_start.get_rect()
                quit_rect = text_quit.get_rect()

                screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
                screen.blit(text_start, (screen_width / 4 * 3 - (start_rect[2] / 2), 300))
                screen.blit(text_quit, (screen_width / 4 * 3 - (quit_rect[2] / 2), 360))
                pygame.display.update()
                clock.tick(FPS)
                pygame.display.set_caption("IN WONDERLAND")

        #Initialize the Game
        main_menu()
        pygame.quit()
        quit()

m = Main_menu()