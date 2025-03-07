# All imports 
import pygame as pg
from random import randint
import sys

# initalizing pygame module
pg.init()
clock = pg.time.Clock()

# colors 
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
gray = (35, 35, 35)
red = (255, 0, 0)

# GameVariables
score = 0
foodx, foody = randint(2, 38), randint(2, 38)
snkx, snky = 4, 4
velox, veloy = 0, 0
running = True
gameover = True
screenx, screeny = 1000, 1000
score = 0
snakeList = []
snkLength = 5


# initialzing game window
screen = pg.display.set_mode((screenx, screeny))
pg.display.set_caption("Snakes with TheCodeee")

def food():
    pg.draw.rect(screen, red, [foodx * 25, foody * 25, 25, 25], border_radius=10)

def plot_snake(snakelist):
    for x, y in snakelist:
        pg.draw.rect(screen, green, pg.Rect(x * 25, y * 25, 25, 25), border_radius=15)
        pg.draw.rect(screen, white, pg.Rect(x * 25, y * 25, 25, 25), width = 4, border_radius = 5)

def gameScreen():
    for i in range(1, screenx // 25):
        pg.draw.line(screen, gray, (i * 25, 0), (i * 25, screeny))
        pg.draw.line(screen, gray, (0, i * 25), (screenx, i * 25))
    
    plot_snake(snakeList)

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
            gameover = False

    screen.fill(black)
    bg = pg.image.load("start.webp")
    bg = pg.transform.scale(bg, (screenx, screeny)).convert_alpha()
    screen.blit(bg, (0, 0))

    while not gameover:
        screen.fill(black)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                if (event.key == pg.K_RIGHT or event.key == pg.K_d) and velox != -1:
                    velox = 1
                    veloy = 0

                if (event.key == pg.K_LEFT or event.key == pg.K_a) and velox != 1:
                    velox = -1
                    veloy = 0

                if (event.key == pg.K_DOWN or event.key == pg.K_s) and veloy != -1:
                    veloy = 1
                    velox = 0

                if (event.key == pg.K_UP or event.key == pg.K_w) and veloy != 1:
                    veloy = -1
                    velox = 0

        food()
        snkx += velox
        snky += veloy

        head = []
        head.append(snkx)
        head.append(snky)

        snakeList.append(head)

        if head[0] < 0 or head[0] > 39 or head[1] < 0 or head[1] > 39:
            score = 0
            foodx, foody = randint(2, 38), randint(2, 38)
            snkx, snky = 4, 4
            velox, veloy = 0, 0
            gameover = True
            score = 0
            snakeList = []
            snkLength = 5

        if head[0] == foodx and head[1] == foody:
            foodx, foody = randint(2, 38), randint(2, 38)
            snkLength += 1
            score += 1
        
        pg.draw.rect(screen, black, pg.Rect(snkx * 25, snky * 25, 25, 25), border_radius=15)
        if len(snakeList) > snkLength:
            del snakeList[0]

        gameScreen()
        pg.display.update()
        clock.tick(30)
    pg.display.update()

pg.quit()
sys.exit()
game = gameLogic()
