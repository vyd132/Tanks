import random

import pygame

show_rects=False

rects=[]

blocks=10
for line in range(blocks):
    size=random.randint(10,100)
    brick=pygame.rect.Rect([random.randint(10,100),random.randint(10,100),size])
    rects.append(brick)

def click_check(cord):
    for line in rects:
        res=line.collidepoint(cord)
        if res:
            print('work')
def model():
    pass




