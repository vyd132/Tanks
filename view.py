import random

import pygame,model
pygame.init()
screen=pygame.display.set_mode([1000,1000])
brick=pygame.image.load('sprites/battle_city_items/block_brick.png')
steel=pygame.image.load('sprites/battle_city_items/block_steel.png')
bullet=pygame.image.load('sprites/battle_city_items/bullet.png')
bullet=pygame.transform.scale(bullet,[6,8])

def view():
    global screen,brick,steel
    screen.fill([0, 0, 0])
    for line in model.rects:
        if line['type']=='brick':
            block = pygame.transform.scale(brick, [line['rect'].w, line['rect'].h])
        else:
            block = pygame.transform.scale(steel, [line['rect'].w, line['rect'].h])
        screen.blit(block, line['rect'])
    pygame.display.flip()
