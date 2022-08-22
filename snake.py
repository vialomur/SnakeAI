import random
WIDTH = 900
HEIGHT = 600
import pygame
pygame.init()
# make the x position, y position, width and the height of the rectangle
width = 60
height = 60
x_pos = width * 3
y_pos = height * 3
JEDZ_WIDTH = 840
JEDZ_HEIGHT = 560
# make the rectangle variable
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4


# now add this to a surface, add a colour and the rectangle and make it a function
def make_food():
    rectangle = pygame.Rect(random.randrange(0,JEDZ_WIDTH,120),random.randrange(0,JEDZ_HEIGHT,80), 20, 20)
    #rectangle = pygame.Rect(480,160,20,20)
    return rectangle

def make_rect(surface, rectangle):
    pygame.draw.rect(surface, (255, 0, 0), rectangle)


def check_borders(rectangle,x_push,y_push,move):
    zwraca = 0
    if move == LEFT or move == RIGHT:
        if rectangle.x >= 0 and rectangle.x <= WIDTH - width:
            rectangle.x += x_push

        if rectangle.x < 0 or rectangle.x > WIDTH-width:
            rectangle.x = width * 7
            rectangle.y = height * 5
            zwraca = -1

        if rectangle.y < 0 or rectangle.y > HEIGHT- height:
            rectangle.x = width * 7
            rectangle.y = height * 5
            zwraca = -1

    if move == UP or move == DOWN:
        if rectangle.y >= 0 and rectangle.y <= HEIGHT - height:
            rectangle.y += y_push

        if rectangle.y < 0 or rectangle.y > HEIGHT- height:
            rectangle.x = width * 7
            rectangle.y = height * 5
            zwraca = -1

        if rectangle.x < 0 or rectangle.x > WIDTH-width:
            rectangle.x = width * 7
            rectangle.y = height * 5
            zwraca = -1

    return zwraca