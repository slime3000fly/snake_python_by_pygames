# snake game with pygame
# By: slime3000fly and a little bit by angater1

import pygame, sys, time, random

pygame.init()
pygame.display.init()
fps_controller = pygame.time.Clock()

screen = pygame.display.set_mode((1080, 720))

# initial score
score = 0

# reading highest score from txt
f = open('highest_score.txt', 'r')
highest_score = int(f.read())
f.close()

#color
black = (0, 0, 0)

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score) + ' ' + 'Highest Score : ' + str(highest_score), True,
                                      color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)

# variable declartaion
x = [200]
y = [200]
checker = [0]
number_of_apple = 0
size = 1  # variable which define how long is snake
t = 0.5
z1 = 0
z2 = 0
move = 20  # variable which define how big is single step for snake
x_apple = 0
y_apple = 0

# function declaration
def lose():
    # function which play after lose game
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.QUIT: sys.exit()
        # drawing writing 'you lose'
        font = pygame.font.Font('freesansbold.ttf', 52)
        text = font.render('YOU LOSE', True, red, white)
        # text surface object
        textRect = text.get_rect()
        # set the center of the rectangular object.
        textRect.center = (540, 360)
        screen.blit(text, textRect)
        pygame.display.update()

def touch():
    # function to check if snake touch itself or wall
    snake_head_x = x[0]
    snake_head_y = y[0]
    # check if snake is colliding itself
    for i in range(1, size):
        for k in range(0, 11):
            if (snake_head_x == x[i] + k):
                for k in range(0, 11):
                    if (snake_head_y == y[i] + k): lose()
    # check if snake is touching wall
    if snake_head_x >= 1060 or snake_head_x <= 20 or snake_head_y >= 700 or snake_head_y <= 20:
        lose()

# color
red = pygame.Color(139, 0, 0)
blue = pygame.Color(51, 255, 255)
white = pygame.Color(255, 255, 255)
orange = (255, 100, 0)
yellow = (255, 50, 170)

done = False

while not done:
    # print(size)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    # adding new element to list x and y
    for i in range(0, size):
        if (i >= len(x)):
            x.append(i)
            y.append(i)

    touch()
    # key to control snake
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            z1 = - move
            z2 = 0
        if event.key == pygame.K_DOWN:
            z1 = move
            z2 = 0
        if event.key == pygame.K_RIGHT:
            z2 = move
            z1 = 0
        if event.key == pygame.K_LEFT:
            z2 = - move
            z1 = 0
        if event.key == pygame.K_ESCAPE:
            done = True

    # nubmer to move snake
    x[0] = x[0] + z2
    y[0] = y[0] + z1

    # create x and y for drawing apple
    if number_of_apple == 0:
        x_apple = random.randint(50, 1000)
        y_apple = random.randint(50, 650)
        number_of_apple = 1

    screen.fill(white)
    # drawing snake
    i = 0
    for i in range(0, size):
        # drawing snake head
        if (i == 0): snake_head = pygame.draw.rect(screen, yellow, pygame.Rect(x[i], y[i], 20, 20))
        # drawing another part of snake
        if (i == 1):
            temp_x2 = x[i]
            temp_y2 = y[i]
            x[i] = previos_x
            y[i] = previos_y
            pygame.draw.rect(screen, blue, pygame.Rect(x[i], y[i], 20, 20))
        if (i >= 2):
            if (i % 2 == 0):
                temp_x1 = x[i]
                x[i] = temp_x2
                temp_y1 = y[i]
                y[i] = temp_y2
                pygame.draw.rect(screen, blue, pygame.Rect(x[i], y[i], 20, 20))
            else:
                temp_x2 = x[i]
                x[i] = temp_x1
                temp_y2 = y[i]
                y[i] = temp_y1
                pygame.draw.rect(screen, blue, pygame.Rect(x[i], y[i], 20, 20))

    # draw apple
    pygame.draw.rect(screen, red, pygame.Rect(x_apple, y_apple, 10, 10))

    # drawing wall
    pygame.draw.rect(screen, orange, pygame.Rect(0, 0, 20, 720))
    pygame.draw.rect(screen, orange, pygame.Rect(1070, 0, 20, 720))
    pygame.draw.rect(screen, orange, pygame.Rect(0, 0, 1080, 20))
    pygame.draw.rect(screen, orange, pygame.Rect(0, 710, 1080, 20))
    # drawing score
    show_score(1, black, 'times new roman', 20)

    pygame.display.flip()

    # check if snake eat apple
    for i in range(-17, 16):
        if x[0] + i == x_apple:
            for i in range(-17, 16):
                if y[0] + i == y_apple:
                    number_of_apple = 0
                    size += 1
                    score += 10
                    if score > highest_score:
                        highest_score = score
    #saving highest score to highest_score.txt
    f = open('highest_score.txt', 'w')
    f.write(str(highest_score))
    f.close()

    # FPS !!!!!
    fps_controller.tick(15)

    previos_x = x[0]
    previos_y = y[0]
