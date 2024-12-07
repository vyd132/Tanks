import random

import pygame,rect_helper,block_helper,tank_helper

import animation_helper
import bullet_helper
import levels
import messenger
import sounds


def objects_move():
    for bullets_dict in  bullets:
        shot=bullet_helper.bullet_fly(bullets_dict,rects,tanks)
        if shot:
            bullets.remove(bullets_dict)
    for tank_dict in tanks:
        tank_dict['rect'].x += tank_dict['speedx']
        tank_dict['rect'].y += tank_dict['speedy']
        tank_dict['speedx'] /= 1.1
        tank_dict['speedy'] /= 1.1
        for line in rects:
            for rect in line['rects']:
                if rect.colliderect(tank_dict['rect']):
                    if tank_dict['rect'].left < rect.right and tank_dict['angle'] == 270:
                        tank_dict['rect'].left = rect.right
                        continue
                    if tank_dict['rect'].right > rect.left and tank_dict['angle'] == 90:
                        tank_dict['rect'].right = rect.left
                        continue
                    if tank_dict['rect'].top < rect.bottom and tank_dict['angle'] == 0:
                        tank_dict['rect'].top = rect.bottom
                        continue
                    if tank_dict['rect'].bottom > rect.top and tank_dict['angle'] == 180:
                        tank_dict['rect'].bottom = rect.top
                        continue

def animation_change():
    for effect_dict in effects:
        animation_helper.anim_change(effect_dict,effects)

def map_create(karta):
    rects=[]
    karta_def=karta.split('\n')
    map_size = len(karta.split('\n'))
    for map in range(len(karta_def)):
        type_block_list=karta_def[map]
        for block in range(len(type_block_list)):
            if type_block_list[block]=='0':
                continue
            brick=block_helper.block_create(type_block_list[block],map_size,block,map)
            rects.append(brick)
    return rects

def model_messeges(type_mes, who, addons):
    global rects
    if type_mes=='tank_died':
        animation_helper.create(effects,who['rect'].centerx,who['rect'].centery,anim_list_dict_big,3)
    if type_mes=='steel not breaked':
        animation_helper.create(effects,addons.centerx,addons.centery,anim_list_dict_small,1)
    if type_mes=='level_changed':
        rects=map_create(who['map'])
        tank_helper.pos_change(who['x'],who['y'],t1)
        tank_helper.angle_change(t1,who['t_angle'])
        bullets.clear()
        effects.clear()
        tank_helper.bullets_clear(t1)






show_rects=False
show_image=True

# Карта
karta="""00011220
01222100
12000111
02211012
02101021
01212000
11112220
20221100"""
# karta="""010
# 002
# 100"""
map_size=len(karta.split('\n'))
rects=map_create(karta)


anim_list_dict_big = []
anim_list_dict_small = []

animation_helper.image_create(map_size,700,anim_list_dict_big)
animation_helper.image_create(map_size,200,anim_list_dict_small)
messenger.add_subs(model_messeges)



# Подоготовка танка
t1=tank_helper.tank_create(0,0,'player','purple',map_size,18,2)
t2=tank_helper.tank_create(5,4,'player','yellow',map_size,2,0)
t3=tank_helper.tank_create(0,3,'enemy','yellow',map_size,1,3)
t4=tank_helper.tank_create(1,7,'enemy','green',map_size,4,3)
tanks=[t1,t2,t3,t4]
bullets=[]
effects=[]

levels.level_change(1)

