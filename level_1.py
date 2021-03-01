import pygame
from random import randrange as rnd
from the_end import game_over, next_level
from pygame.locals import *
import os


number_of_level = 1
fps = 60
paddle_w = 300
AGAIN = False


def level():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    WIDTH, HEIGHT = 1010, 600

    global number_of_level, fps, paddle_w, AGAIN
    if not AGAIN:
        paddle_w = max(100, paddle_w - 10)
        number_of_level += 1
        fps += 1
    else:
        number_of_level = 1
        fps = 60
        paddle_w = 300
        AGAIN = False

    co = 0


    paddle_h = 25
    paddle_speed = 15
    paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)

    ball_radius = 20
    ball_speed = 6
    ball_rect = int(ball_radius * 2 ** 0.5)
    ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
    dx, dy = 1, -1

    block_list = [pygame.Rect(10 + 100 * i, 10 + 60 * j, 90, 40) for i in range(10) for j in range(4)]

    pygame.init()
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    # сюда вставь что нибудь для фона, когда будешь оформлять
    img = pygame.image.load('1.jpg').convert()


    def dc(dx, dy, ball, rect):
        if dx > 0:
            delta_x = ball.right - rect.left
        else:
            delta_x = rect.right - ball.left
        if dy > 0:
            delta_y = ball.bottom - rect.top
        else:
            delta_y = rect.bottom - ball.top

        if abs(delta_x - delta_y) < 10:
            dx, dy = -dx, -dy
        elif delta_x > delta_y:
            dy = -dy
        elif delta_y > delta_x:
            dx = -dx
        return dx, dy


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        sc.blit(img, (0, 0))

        [pygame.draw.rect(sc, "blue", block) for color, block in enumerate(block_list)]
        pygame.draw.rect(sc, pygame.Color('white'), paddle)
        pygame.draw.circle(sc, pygame.Color('red'), ball.center, ball_radius)

        ball.x += ball_speed * dx
        ball.y += ball_speed * dy

        if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
            dx = -dx

        if ball.centery < ball_radius:
            dy = -dy

        if ball.colliderect(paddle) and dy > 0:
            dx, dy = dc(dx, dy, ball, paddle)


        hit_index = ball.collidelist(block_list)
        if hit_index != -1:
            hit_rect = block_list.pop(hit_index)
            dx, dy = dc(dx, dy, ball, hit_rect)
            co = 40 - len(block_list)
            hit_rect.inflate_ip(ball.width * 3, ball.height * 3)
            fps += 1

        if ball.bottom > HEIGHT:
            if game_over(number_of_level, co):
                AGAIN = True
                level()

        elif not len(block_list):
            if next_level(number_of_level):
                level()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddle_speed
        if key[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.right += paddle_speed

        font = pygame.font.Font(None, 60)
        text = font.render(str(co), 1, (100, 255, 100))
        sc.blit(text, (10, 550))
        pygame.display.flip()
        clock.tick(fps)