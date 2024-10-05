import random

import pygame,model,block_helper

def tank_change(tank_dict):
    tank = pygame.transform.rotate(tank_dict["image"], -tank_dict["angle"])
    tank = pygame.transform.scale(tank, tank_dict["rect"].size)
    return tank

def tanks_save():
    for tanks in model.tanks:
        tank = tank_change(tanks)
        tanks['image_view'] = tank

def bullet_change(bullet_dict):
    bullet= pygame.transform.rotate(bullet_dict["image"], -bullet_dict["angle"])
    bullet = pygame.transform.scale(bullet, bullet_dict["rect"].size)
    return bullet

def bullet_save():
    for bullets in model.bullets:
        if 'image_view' in bullets:
            continue
        bullet_new = tank_change(bullets)
        bullets['image_view'] = bullet_new

def view():
    global screen,brick,steel,tank,tank2
    screen.fill([0, 0, 0])
    for line in model.rects:
        block_image=block_helper.image_block_create(line)
        screen.blit(block_image,line['final_rect'])

        for block in line['rects']:

            if model.show_rects:
                pygame.draw.rect(screen,[255,0,0],block,width=1)
    if model.changes:
        bullet_save()
        tanks_save()
    if model.show_image:
        for bullet in model.bullets:
            screen.blit(bullet['image_view'], bullet['rect'])
        # pygame.image.save(model.t2["image"],'tank_test.png')
        # print(model.t1["rect"])
        for tanks in model.tanks:
            screen.blit(tanks['image_view'], tanks["rect"])
        # print(tank.get_size(), model.tank.size)
    if model.show_rects:
        for bullet in model.bullets:
            pygame.draw.rect(screen, [255, 255, 0], bullet["rect"], width=1)
        for tanks in model.tanks:
            pygame.draw.rect(screen, [255, 255, 0], tanks["rect"], width=1)
    pygame.display.flip()



pygame.init()
screen=pygame.display.set_mode([1000,1000])

brick=pygame.image.load('sprites/battle_city_items/block_brick.png')
steel=pygame.image.load('sprites/battle_city_items/block_steel.png')
bullet=pygame.image.load('sprites/battle_city_items/bullet.png')

bullet_image=pygame.transform.scale(bullet,[6,8])

tanks_save()