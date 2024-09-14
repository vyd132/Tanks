import random

import pygame,model

def tank_change(tank_dict):
    tank = pygame.transform.rotate(tank_dict["image"], -tank_dict["angle"])
    tank = pygame.transform.scale(tank, tank_dict["rect"].size)
    return tank

def tanks_save():
    for tanks in model.tanks:
        tank = tank_change(tanks)
        tanks['image_view'] = tank



pygame.init()
screen=pygame.display.set_mode([1000,1000])
brick=pygame.image.load('sprites/battle_city_items/block_brick.png')
steel=pygame.image.load('sprites/battle_city_items/block_steel.png')

bullet=pygame.image.load('sprites/battle_city_items/bullet.png')
bullet=pygame.transform.scale(bullet,[6,8])

tanks_save()


def view():
    global screen,brick,steel,tank,tank2
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
        tanks_save()
    if model.show_image:
        # pygame.image.save(model.t2["image"],'tank_test.png')
        # print(model.t1["rect"])
        for tanks in model.tanks:
            screen.blit(tanks['image_view'], tanks["rect"])
        # print(tank.get_size(), model.tank.size)
    if model.show_rects:
        for tanks in model.tanks:
            pygame.draw.rect(screen, [255, 255, 0], tanks["rect"], width=1)





    pygame.display.flip()
