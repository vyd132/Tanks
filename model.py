import random

import pygame

show_rects=False
show_image=True
build=True
karta="""
00011220
01222100
12000111
02211012
02101021
01212000
11112220
20221100
"""
rects=[]
x=0
map_size=8
for map in karta:
    for line in range(map_size):

        size = 1000 / map_size
        y = 0
        if map == '0':
            x += 1000 / map_size
            build=False
        if map == '1':
            build = True
            brick=pygame.rect.Rect([x,y,size,size])
            block={'rect':brick,'type':'brick'}
            rects.append(block)
            x += 1000 / map_size
            print(x)
        if map=='2':
            build = True
            brick = pygame.rect.Rect([x, y, size, size])
            block = {'rect': brick, 'type': 'steel'}
            rects.append(block)
            # print(brick)
            x += 1000 / map_size



def click_check(cord):
    for line in rects:
        res=line.collidepoint(cord)
        if res:
            print('work')
def model():
    pass




