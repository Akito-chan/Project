import pygame
from pygame.locals import *
import os
import random



def game_over(n, co):
    pygame.init()
    WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 400, 400

    # Center the Game Application
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Game Resolution
    screen_width = 400
    screen_height = 400
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

    # Main Menu
    def main_menu():

        menu = True
        selected = "start"

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = "start"
                    elif event.key == pygame.K_DOWN:
                        selected = "quit"
                    if event.key == pygame.K_RETURN:
                        if selected == "start":
                            return True
                        if selected == "quit":
                            return False

            # Main Menu UI
            screen.fill(blue)
            title = text_format("IN WONDERLEND", font1, 40, yellow)
            if selected == "start":
                text_start = text_format("Play again", font, 40, white)
            else:
                text_start = text_format("Play again", font, 40, black)
            if selected == "quit":
                text_quit = text_format("Quit", font, 40, white)
            else:
                text_quit = text_format("Quit", font, 40, black)
            counter = text_format(str(co), font, 140, white)


            title_rect = title.get_rect()
            start_rect = text_start.get_rect()
            quit_rect = text_quit.get_rect()
            counter_rect = counter.get_rect()

            screen.blit(counter, (screen_width / 2 - (counter_rect[2] / 2), 90))

            screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 10))
            screen.blit(text_start, (screen_width / 2 - (start_rect[2] / 2), 290))
            screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 340))
            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("Blueberry")

    # Initialize the Game
    re = main_menu()
    if re:
        return True
    else:
        return False
    pygame.quit()
    quit()


def next_level(n):
    pygame.init()
    WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 400, 400

    # Center the Game Application
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Game Resolution
    screen_width = 400
    screen_height = 400
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




    # Main Menu
    def main_menu():

        menu = True
        selected = "start"

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = "start"
                    elif event.key == pygame.K_DOWN:
                        selected = "quit"
                    if event.key == pygame.K_RETURN:
                        if selected == "start":
                            return True
                        if selected == "quit":
                            return False

            # Main Menu UI
            screen.fill(blue)
            title = text_format("IN WONDERLEND", font1, 40, yellow)
            if selected == "start":
                text_start = text_format("Next level", font, 40, white)
            else:
                text_start = text_format("Next level", font, 40, black)
            if selected == "quit":
                text_quit = text_format("Quit", font, 40, white)
            else:
                text_quit = text_format("Quit", font, 40, black)
            counter = text_format('Winning!', font, 100, white)

            title_rect = title.get_rect()
            start_rect = text_start.get_rect()
            quit_rect = text_quit.get_rect()
            counter_rect = counter.get_rect()

            screen.blit(counter, (screen_width / 2 - (counter_rect[2] / 2), 90))

            screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 10))
            screen.blit(text_start, (screen_width / 2 - (start_rect[2] / 2), 290))
            screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 340))
            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("Blueberry")

    # Initialize the Game
    re = main_menu()
    if re:
        return True
    else:
        return False
    pygame.quit()
    quit()