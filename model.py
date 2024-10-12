import random

import pygame,rect_helper,block_helper

import bullet_helper


def costume_list_gen(type,color):
    tank_list=[]
    for size in range(1,5):
        tank_list.append('sprites/battle_city_tanks/tank_'+type+'_size'+str(size)+'_'+color+'1.png')
    return tank_list

def tank_create(x,y,type,color):
    tank = pygame.rect.Rect([0, 0, 0, 0])
    costumes=costume_list_gen(type,color)
    image = pygame.image.load(costumes[0])
    t1 = {
        "rect": tank,
        'costumes': costumes,
        'image': image,
        'costume_number': 0,
        'angle': 0,
        "speedx": 0,
        "speedy": 0
    }
    rect_helper.rect_change(t1['rect'], t1['angle'] == 0, t1['image'], original_width, True)
    tank.centerx = (1000 / map_size) * x + (1000 / map_size) / 2
    tank.centery = 1000 / map_size * y + (1000 / map_size) / 2
    return t1



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




def tank_angle_and_move(angle2,speedx2,speedy2,tank_dict):
    global angle,speedx,speedy,changes
    tank_dict['angle'] = angle2
    tank_dict['speedx'] = speedx2
    tank_dict['speedy'] = speedy2
    rect_helper.rect_change(tank_dict['rect'], tank_dict['angle'] in [0,180], tank_dict["image"], original_width, True)
    changes = True
def change_costume(tank_dict):
    global changes
    tank_dict["image"]=pygame.image.load(tank_dict['costumes'][tank_dict['costume_number']])
    rect_helper.rect_change(tank_dict['rect'], tank_dict['angle'] in [0,180], tank_dict["image"], original_width, True)
    tank_dict['costume_number']+=1
    changes = True
    if tank_dict['costume_number']==len(tank_dict['costumes']):
        tank_dict['costume_number']=0

def model(tank_dict):
    global speedx,speedy,changes
    changes=False
    tank_dict['rect'].x+=tank_dict['speedx']
    tank_dict['rect'].y+=tank_dict['speedy']
    tank_dict['speedx'] = 0
    tank_dict['speedy']=0
    for bullets_dict in  bullets:
        shot=bullet_helper.bullet_fly(bullets_dict,rects)
        if shot:
            bullets.remove(bullets_dict)
    for line in rects:
        for rect in line['rects']:
            if rect.colliderect(tank_dict['rect']):
                if tank_dict['rect'].left<rect.right and tank_dict['angle']==270:
                    tank_dict['rect'].left=rect.right
                    continue
                if tank_dict['rect'].right > rect.left and tank_dict['angle']==90:
                    tank_dict['rect'].right = rect.left
                    continue
                if tank_dict['rect'].top < rect.bottom and tank_dict['angle']==0:
                    tank_dict['rect'].top = rect.bottom
                    continue
                if tank_dict['rect'].bottom > rect.top and tank_dict['angle'] == 180:
                    tank_dict['rect'].bottom = rect.top
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
# karta="""010
# 002
# 100"""
map_size=len(karta.split('\n'))
rects=map_create(karta)




# Подоготовка танка
original_width = 500 / map_size
t1=tank_create(0,0,'player','purple')
t2=tank_create(5,4,'player','white')
t3=tank_create(0,3,'enemy','yellow')
t4=tank_create(1,7,'enemy','green')
tanks=[t1,t2,t3,t4]
bullets=[]
print(t1)




