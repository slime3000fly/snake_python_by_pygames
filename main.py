import pygame, sys, time, random

pygame.init()
pygame.display.init()
fps_controller = pygame.time.Clock()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1080, 720))

x = [200]
y = [200]
checker = [0]
z1 = 0
z2 = 0
move = 20  # variable which define how big is single step for snake
lose = 0
number_of_apple = 0
size = 1  # variable which define how long is snake
t = 0.5
g=10
j=10

# color
red = pygame.Color(139, 0, 0)
blue = pygame.Color(51, 255, 255)
white = pygame.Color(255, 255, 255)
orange = (255, 100, 0)
yellow = (255, 50, 170)

x_apple = 0
y_apple = 0

done = False

while not done:

    while lose == 0:
        #print(size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # adding new element to list x and y
        for i in range(0, size):
            if (i >= len(x)):
                x.append(i)
                y.append(i)

        if x[0] >= 1040 or x[0] <= 10 or y[0] >= 700 or y[0] <= 10: lose = 1  # check if snake touch wall
        # check if snake is touching itself
        snake_head_x = x[0]
        snake_head_y = y[0]
        # check if snake is colliding itself
        for k in range(1, size):


            if snake_head_x <= x[k] + g:
                if snake_head_y <= y[k] + j:
                    lose = 1
                    print(lose)
                    print('gowno')
            print(x[k]+g,y[k]+j,snake_head_x,snake_head_y)

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
                lose = 1

        # nubmer to move snake
        x[0] = x[0] + z2
        y[0] = y[0] + z1

        # create x and y for drawing apple
        if number_of_apple == 0:
            x_apple = random.randint(20, 1060)
            y_apple = random.randint(20, 700)
            number_of_apple = 1

        screen.fill(white)
        # drawing snake
        # TODO: zrob zeby rysowalo sie w zaleznosci od ruchu snake podczas ruchu nie zjedzenia jablka
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
                if (x[i - 1] < x[i]): x[i] -= 20 - move
                if (x[i - 1] > x[i]): x[i] += 20 - move
                if (y[i - 1] < y[i]): y[i] -= 20 - move
                if (y[i - 1] > y[i]): y[i] += 20 - move
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
        pygame.draw.rect(screen, orange, pygame.Rect(0, 0, 10, 720))
        pygame.draw.rect(screen, orange, pygame.Rect(1070, 0, 10, 720))
        pygame.draw.rect(screen, orange, pygame.Rect(0, 0, 1080, 10))
        pygame.draw.rect(screen, orange, pygame.Rect(0, 710, 1080, 10))

        pygame.display.flip()

        # check if snake eat apple
        i = 0
        for i in range(-21, 21):
            if (x[0] + i == x_apple):
                for i in range(-21, 21):
                    if (y[0] + i == y_apple):
                        number_of_apple = 0
                        size += 10

        # FPS !!!!!
        fps_controller.tick(12)

        previos_x = x[0]
        previos_y = y[0]

    # #after lose game
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                lose = 0
    # drawing writing 'you lose'
    font = pygame.font.Font('freesansbold.ttf', 52)
    text = font.render('YOU LOSE', True, red, white)
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (1080 // 2, 720 // 2)

    screen.blit(text, textRect)

    pygame.display.update()
