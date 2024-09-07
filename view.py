import random

import pygame,model
pygame.init()
screen=pygame.display.set_mode([1000,1000])
brick=pygame.image.load('sprites/battle_city_items/block_brick.png')
steel=pygame.image.load('sprites/battle_city_items/block_steel.png')

bullet=pygame.image.load('sprites/battle_city_items/bullet.png')
bullet=pygame.transform.scale(bullet,[6,8])

tank = pygame.transform.rotate(model.tank_image, -model.angle)
tank = pygame.transform.scale(tank, model.tank.size)


def view():
    global screen,brick,steel,tank
    screen.fill([0, 0, 0])
    for line in model.rects:
        if line['type']=='brick':
            block = pygame.transform.scale(brick, [line['rect'].w, line['rect'].h])
        else:
            block = pygame.transform.scale(steel, [line['rect'].w, line['rect'].h])
        if model.show_image:
            screen.blit(block, line['rect'])
        if model.show_rects:
            pygame.draw.rect(screen,[255,0,0],line['rect'],width=1)
    if model.changes:
        tank = pygame.transform.rotate(model.tank_image, -model.angle)
        tank = pygame.transform.scale(tank, model.tank.size)
    if model.show_image:
        screen.blit(tank, model.tank)
        # print(tank.get_size(), model.tank.size)
    if model.show_rects:
        pygame.draw.rect(screen, [255, 255, 0], model.tank, width=1)




    pygame.display.flip()
