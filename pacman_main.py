from typing import List, Union
# from pygame import font
import pygame
import os, sys
import math

from pygame import Surface, SurfaceType , font

# create display of pacman game
boards = [
    [6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
    [3, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 3],
    [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
    [3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
    [3, 3, 2, 3, 0, 0, 3, 1, 3, 0, 0, 0, 3, 1, 3, 3, 1, 3, 0, 0, 0, 3, 1, 3, 0, 0, 3, 2, 3, 3],
    [3, 3, 1, 7, 4, 4, 8, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 7, 4, 4, 8, 1, 3, 3],
    [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
    [3, 3, 1, 6, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 5, 1, 3, 3],
    [3, 3, 1, 7, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 8, 1, 3, 3],
    [3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
    [3, 7, 4, 4, 4, 4, 5, 1, 3, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 3, 1, 6, 4, 4, 4, 4, 8, 3],
    [3, 0, 0, 0, 0, 0, 3, 1, 3, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 3, 1, 3, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
    [8, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 9, 9, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 7],
    [4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4],
    [5, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 6],
    [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
    [3, 6, 4, 4, 4, 4, 8, 1, 7, 8, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 7, 8, 1, 7, 4, 4, 4, 4, 5, 3],
    [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
    [3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
    [3, 3, 1, 7, 4, 5, 3, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 3, 6, 4, 8, 1, 3, 3],
    [3, 3, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 3],
    [3, 7, 4, 5, 1, 3, 3, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 3, 3, 1, 6, 4, 8, 3],
    [3, 6, 4, 8, 1, 7, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 8, 1, 7, 4, 5, 3],
    [3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
    [3, 3, 1, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 1, 3, 3],
    [3, 3, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 3],
    [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
    [3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
    [7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]
]
pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("PACMAN GAME")
timer = pygame.time.Clock()
fps = 60
levels = boards
colour = 'blue'
player_img = []
PI = math.pi
player_images = []
for i in range(1, 5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'Assets/player_images/{i}.png'), (40, 40)))
player_X = 480
player_Y = 610
direction = 0
counter = 0
flicker = False
centerX = player_X + 23
centerY = player_Y + 24
# right,left,up,down
turnsAllowed = [False, False, False, False]
direction_command = 0
player_speed = 2
score= 0


# ttf_path = os.path.join(sys.path[0], "freesanbold.ttf")
# pygame.font.Font(ttf_path, 20)
# font= pygame.font.Font('',20)
def draw_mics():
    score_text= font.render(f'score: {score}',True,'white')
    screen.blit(score_text,(10,920))
def check_collision(scor):
    num1 = ((screen_height-50)//32)
    num2 =screen_width//30
    if 0< player_X <870:
        if levels[centerY//num1][centerX//num2]==1:
            levels[centerY//num1][centerX//num2]=0
            scor+=50
        if levels[centerY//num1][centerX//num2]==2:
            levels[centerY//num1][centerX//num2]=0
            scor+=50
    return scor

def draw_board():
    num1 = ((screen_height - 50) // 32)
    num2 = (screen_width // 30)
    for i in range(len(levels)):
        for j in range(len(levels[i])):
            if levels[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            if levels[i][j] == 2 and not flicker:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            if levels[i][j] == 3:
                pygame.draw.line(screen, colour, (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            if levels[i][j] == 4:
                pygame.draw.line(screen, colour, (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            if levels[i][j] == 5:
                pygame.draw.arc(screen, colour, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                0, PI / 2, 3)
            if levels[i][j] == 6:
                pygame.draw.arc(screen, colour,
                                [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
            if levels[i][j] == 7:
                pygame.draw.arc(screen, colour, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI,
                                3 * PI / 2, 3)
            if levels[i][j] == 8:
                pygame.draw.arc(screen, colour,
                                [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2,
                                2 * PI, 3)
            if levels[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)


def move_player(play_x, play_y):
    if direction == 0 and turnsAllowed[0]:
        play_x += player_speed
    elif direction == 1 and turnsAllowed[1]:
        play_x -= player_speed
    elif direction == 2 and turnsAllowed[2]:
        play_y -= player_speed
    elif direction == 3 and turnsAllowed[3]:
        play_y += player_speed
    return play_x, play_y



def check_position(centerX, centerY):
    turns = [False, False, False, False]
    num1 = (screen_height - 50) // 32
    num2 = (screen_width // 30)
    num3 = 15
    # check collisions based on center x and center y of player +/- fudge number
    if centerX // 30 < 29:
        if direction == 0:
            if levels[centerY // num1][(centerX - num3) // num2] < 3:
                turns[1] = True
        if direction == 1:
            if levels[centerY // num1][(centerX + num3) // num2] < 3:
                turns[0] = True
        if direction == 2:
            if levels[(centerY + num3) // num1][centerX // num2] < 3:
                turns[3] = True
        if direction == 3:
            if levels[(centerY - num3) // num1][centerX // num2] < 3:
                turns[2] = True

        if direction == 2 or direction == 3:
            if 12 <= centerX % num2 <= 18:
                if levels[(centerY + num3) // num1][centerX // num2] < 3:
                    turns[3] = True
                if levels[(centerY - num3) // num1][centerX // num2] < 3:
                    turns[2] = True
            if 12 <= centerY % num1 <= 18:
                if levels[centerY // num1][(centerX - num2) // num2] < 3:
                    turns[1] = True
                if levels[centerY // num1][(centerX + num2) // num2] < 3:
                    turns[0] = True
        if direction == 0 or direction == 1:
            if 12 <= centerX % num2 <= 18:
                if levels[(centerY + num1) // num1][centerX // num2] < 3:
                    turns[3] = True
                if levels[(centerY - num1) // num1][centerX // num2] < 3:
                    turns[2] = True
            if 12 <= centerY % num1 <= 18:
                if levels[centerY // num1][(centerX - num3) // num2] < 3:
                    turns[1] = True
                if levels[centerY // num1][(centerX + num3) // num2] < 3:
                    turns[0] = True
    else:
        turns[0] = True
        turns[1] = True

    return turns

def player():
    if direction == 0:
        screen.blit(player_images[counter // 5], (player_X, player_Y))
    elif direction == 1:
        screen.blit(pygame.transform.flip(player_images[counter // 5], True, False), (player_X, player_Y))
    elif direction == 2:
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 90), (player_X, player_Y))
    elif direction == 3:
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 270), (player_X, player_Y))


run = True
while run:
    timer.tick(fps)
    if counter < 19:
        counter += 1
        if counter > 1:
            flicker = False
    else:
        counter = 0
        flicker = True

    screen.fill('black')
    draw_board()
    player()
    draw_mics()
    centerX = player_X + 23
    centerY = player_Y + 24
    turnsAllowed = check_position(centerX, centerY)
    player_X, player_Y = move_player(player_X, player_Y)
    score = check_collision(score)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction_command = 0
            if event.key == pygame.K_LEFT:
                direction_command = 1
            if event.key == pygame.K_UP:
                direction_command = 2
            if event.key == pygame.K_DOWN:
                direction_command = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and direction_command == 0:
                direction_command = direction
            if event.key == pygame.K_LEFT and direction_command == 1:
                direction_command = direction
            if event.key == pygame.K_UP and direction_command == 2:
                direction_command = direction
            if event.key == pygame.K_DOWN and direction_command == 3:
                direction_command = direction

    if direction_command == 0 and turnsAllowed[0]:
        direction = 0
    if direction_command == 1 and turnsAllowed[1]:
        direction = 1
    if direction_command == 2 and turnsAllowed[2]:
        direction = 2
    if direction_command == 3 and turnsAllowed[3]:
        direction = 3
    if player_X > 900:
        player_X = -47
    elif player_X < -50:
        player_X = 897
    pygame.display.flip()
pygame.quit()
