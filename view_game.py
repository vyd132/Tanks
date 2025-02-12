import random

import pygame,model,block_helper,tank_helper,view_main
from view_main import screen

import animation_helper

def view():
    global screen,brick,steel,tank,tank2
    model.mananger.update(1 / 60)
    screen.fill([0, 0, 0])
    for line in model.rects:
        block_image=block_helper.image_block_create(line)
        screen.blit(block_image,line['final_rect'])
        for block in line['rects']:

            if model.show_rects:

                pygame.draw.rect(screen,[255,0,0],block,width=1)

    if model.show_image:
        for effect in model.effects:
            animation_helper.view(effect,screen)
        for bullet in model.bullets:
            screen.blit(bullet['image_view'], bullet['rect'])
        for tanks in model.tanks:
            tank_helper.view(tanks,screen)

    if model.show_rects:
        for bullet in model.bullets:
            pygame.draw.rect(screen, [255, 255, 0], bullet["rect"], width=1)
        for tanks in model.tanks:
            tank_helper.debug_view(tanks,screen)
    model.mananger.draw_ui(view_main.screen)
    pygame.display.flip()





brick=pygame.image.load('sprites/battle_city_items/block_brick.png')
steel=pygame.image.load('sprites/battle_city_items/block_steel.png')
bullet=pygame.image.load('sprites/battle_city_items/bullet.png')

bullet_image=pygame.transform.scale(bullet,[6,8])

