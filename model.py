import random

import pygame,rect_helper,block_helper,tank_helper

import animation_helper
import bullet_helper
import levels
import messenger
import sounds
import tank_ai
from tasks import task_move,task_wait

def objects_move():
    for bullets_dict in  bullets:
        shot=bullet_helper.bullet_fly(bullets_dict,rects,tanks)
        if shot:
            bullets.remove(bullets_dict)

    for tank_dict in tanks:
        tank_ai.comands(tank_dict)
    block_rects=[]
    for block in rects:
        for rect in block['rects']:
            block_rects.append(rect)

    for tank_dict in tanks:
        all_rects=[]
        for tank in tanks:
            if not tank_dict['rect'].colliderect(tank['rect']):
                all_rects.append(tank['rect'])
        all_rects+=block_rects
        tank_helper.tank_move(tank_dict,all_rects)


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
        for lvl_dict in who['enemy_pos']:
            timer_spawn = pygame.event.custom_type()
            pygame.time.set_timer(timer_spawn,lvl_dict['time'])
            lvl_dict['custom_type']=timer_spawn

            timer_wave = pygame.event.custom_type()
            pygame.time.set_timer(timer_wave, lvl_dict['sleep'],1)
            lvl_dict['custom_type_wave'] = timer_wave
        tanks.clear()
        tanks.append(t1)


def search_type(type,lvl):
    for lvl_dict in lvl['enemy_pos']:
        if lvl_dict['custom_type']==type:
            return lvl_dict

def search_type_wave(type,lvl):
    for lvl_dict in lvl['enemy_pos']:
        if lvl_dict['custom_type_wave']==type:
            lvl_dict['wave_start']=True



def enemy_spawn(type):
    search_type_wave(type, levels.levels_list[levels.current_level])
    tank_level_dict=search_type(type,levels.levels_list[levels.current_level])
    if tank_level_dict is None:
        return
    if tank_level_dict['wave_start']!=True or len(tank_level_dict['tanks_list'])==0:
        return
    new_tank=tank_helper.tank_create(tank_level_dict['x'],tank_level_dict['y'],'enemy','white',map_size,3,tank_level_dict['tanks_list'][0])
    del tank_level_dict['tanks_list'][0]
    task_wait.action_create(new_tank['task'],new_tank)
    tanks.append(new_tank)



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



anim_list_dict_big = []
anim_list_dict_small = []

animation_helper.image_create(map_size,700,anim_list_dict_big)
animation_helper.image_create(map_size,200,anim_list_dict_small)
messenger.add_subs(model_messeges)



# Подоготовка танка
t1=tank_helper.tank_create(0,0,'player','purple',map_size,18,2)
t2=tank_helper.tank_create(5,4,'player','yellow',map_size,2,0)

tanks=[t1,t2]
bullets=[]
effects=[]

levels.level_change(1)

active_screen='main'