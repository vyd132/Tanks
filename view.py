import random

import pygame,model
pygame.init()
screen=pygame.display.set_mode([1000,1000])
brick=pygame.image.load('sprites/battle_city_items/block_brick.png')
steel=pygame.image.load('sprites/battle_city_items/block_steel.png')

bullet=pygame.image.load('sprites/battle_city_items/bullet.png')
bullet=pygame.transform.scale(bullet,[6,8])

tank = pygame.transform.rotate(model.t1["image"], -model.t1["angle"])
tank = pygame.transform.scale(tank, model.t1["rect"].size)
tank2 = pygame.transform.rotate(model.t2["image"], -model.t2["angle"])
tank2 = pygame.transform.scale(tank2, model.t2["rect"].size)

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
        tank = pygame.transform.rotate(model.t1["image"], -model.t1["angle"])
        tank = pygame.transform.scale(tank, model.t1["rect"].size)
        tank2 = pygame.transform.rotate(model.t2["image"], -model.t2["angle"])
        tank2 = pygame.transform.scale(tank2, model.t2["rect"].size)
    if model.show_image:
        pygame.image.save(model.t2["image"],'tank_test.png')
        print(model.t1["rect"])
        screen.blit(tank, model.t1["rect"])
        screen.blit(tank2, model.t2["rect"])
        # print(tank.get_size(), model.tank.size)
    if model.show_rects:
        pygame.draw.rect(screen, [255, 255, 0], model.t1["rect"], width=1)
        pygame.draw.rect(screen, [255, 255, 0], model.t2["rect"], width=1)




    pygame.display.flip()
