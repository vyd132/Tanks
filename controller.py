import random

import pygame,model,bullet_helper,tank_helper,animation_helper

import view

pygame.key.set_repeat(100)
timer_move=pygame.event.custom_type()
pygame.time.set_timer(timer_move,10)
timer_anim=pygame.event.custom_type()
pygame.time.set_timer(timer_anim,100)

def event():
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            model.show_rects=not model.show_rects
        # if event.type==pygame.MOUSEBUTTONDOWN:
        #     model.click_check(event.pos)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            model.show_image=not model.show_image

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            animation_helper.create(model.effects,random.randint(0,1000),random.randint(0,1000))


        if event.type==timer_anim:
            model.animation_change()


        if event.type==timer_move:
            model.objects_move()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            tank_helper.up(model.t1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            tank_helper.right(model.t1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            tank_helper.down(model.t1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            tank_helper.left(model.t1)
        if event.type == pygame.KEYUP and event.key == pygame.K_e:
            tank_helper.upgrade(model.t1)
        if event.type == pygame.KEYUP and event.key == pygame.K_r:
            tank_helper.downgrade(model.t1)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            bullet_helper.bullet_spawn(model.t1,model.map_size,model.bullets)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            tank_helper.up(model.t2)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            tank_helper.right(model.t2)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            tank_helper.down(model.t2)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            tank_helper.left(model.t2)
        if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            tank_helper.upgrade(model.t2)

        if event.type == pygame.KEYUP and event.key == pygame.K_f:
            tank_helper.enemy_downgarde(model.t4)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_RIGHT:
            bullet_helper.bullet_spawn(model.t4,model.map_size,model.bullets)
        # if event.type == pygame.KEYUP and event.key == pygame.K_g:
        #     tank_helper.downgrade(model.t4)
        #     model.changes = True

        if event.type == pygame.KEYUP and event.key == pygame.K_t:
            tank_helper.upgrade(model.t3)
        if event.type == pygame.KEYUP and event.key == pygame.K_y:
            tank_helper.downgrade(model.t3)