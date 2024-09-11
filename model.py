import random

import pygame,rect_helper

def map_create():
    cycle = False
    x = 0
    y = 0
    for map in karta:
        if map=='\n':
            y += 1000 / map_size
            x=0
        if cycle:
            continue
        size = 1000 / map_size
        if map == '0':
            x += 1000 / map_size
            # build=False*
            cycle=True
        if map == '1':
            # build = True
            brick=pygame.rect.Rect([x,y,size,size])
            block={'rect':brick,'type':'brick'}
            rects.append(block)
            x += 1000 / map_size
            # print(x)
            cycle = True
        if map=='2':
            # build = True
            brick = pygame.rect.Rect([x, y, size, size])
            block = {'rect': brick, 'type': 'steel'}
            rects.append(block)
            # print(brick)
            x += 1000 / map_size
            cycle = True
        cycle = False

def angle_and_move(angle2,speedx2,speedy2,tank_dict):
    global angle,speedx,speedy,changes
    tank_dict['angle'] = angle2
    speedx = speedx2
    speedy = speedy2

    rect_helper.rect_change(tank_dict['rect'], tank_dict['angle'] in [0,180], tank_dict["image"], original_width, True)
    changes = True

# def rect_change():

def change_costume(tank_dict):
    global changes
    tank_dict["image"]=pygame.image.load(tank_dict['costumes'][tank_dict['costume_number']])
    rect_helper.rect_change(tank_dict['rect'], tank_dict['angle'] in [0,180], tank_dict["image"], original_width, True)#todo
    tank_dict['costume_number']+=1
    changes = True
    if tank_dict['costume_number']==len(tank_dict['costumes']):
        tank_dict['costume_number']=0

def model(tank_dict):
    global speedx,speedy,changes
    changes=False
    tank_dict['rect'].x+=speedx
    tank_dict['rect'].y+=speedy
    speedx=0
    speedy=0
    for line in rects:
        if line['rect'].colliderect(tank_dict['rect']):
            if tank_dict['rect'].left<line['rect'].right and tank_dict['angle']==270:
                tank_dict['rect'].left=line['rect'].right
                continue
            if tank_dict['rect'].right > line['rect'].left and tank_dict['angle']==90:
                tank_dict['rect'].right = line['rect'].left
                continue
            if tank_dict['rect'].top < line['rect'].bottom and tank_dict['angle']==0:
                tank_dict['rect'].top = line['rect'].bottom
                continue
            if tank_dict['rect'].bottom > line['rect'].top and tank_dict['angle'] == 180:
                tank_dict['rect'].bottom = line['rect'].top
                continue

show_rects=False
show_image=True
changes=True

# Карта
karta="""00011220
01222100
12000111
02211012
02101021
01212000
11112220
20221100"""
map_size=len(karta.split('\n'))
rects=[]
map_create()


# Подоготовка танка

speedx=0
speedy=0

tank_color_green=['sprites/battle_city_tanks/tank_player_size1_green1.png', 'sprites/battle_city_tanks/tank_player_size2_green1.png', 'sprites/battle_city_tanks/tank_player_size3_green1.png', 'sprites/battle_city_tanks/tank_player_size4_green1.png']
tank_color_yellow=['sprites/battle_city_tanks/tank_player_size1_yellow1.png','sprites/battle_city_tanks/tank_player_size2_yellow1.png','sprites/battle_city_tanks/tank_player_size3_yellow1.png','sprites/battle_city_tanks/tank_player_size4_yellow1.png']
tank_image_green=pygame.image.load(tank_color_green[0])
tank_image_yellow=pygame.image.load(tank_color_yellow[0])



w=tank_image_green.get_width()
h=tank_image_green.get_height()
tank=pygame.rect.Rect([400,540,0,0])
tank2=pygame.rect.Rect([700,540,0,0])
t1={"rect":tank,'costumes':tank_color_green,'image':tank_image_green,'costume_number':0,'angle':0}
t2={"rect":tank2,'costumes':tank_color_yellow,'image':tank_image_yellow,'costume_number':0,'angle':0}
original_width = 500 / map_size
rect_helper.rect_change(t1['rect'],t1['angle'] ==0,t1['image'],original_width,True)
rect_helper.rect_change(t2['rect'],t2['angle'] ==0,t2['image'],original_width,True)



