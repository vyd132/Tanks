import random

import pygame,rect_helper,block_helper

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

def bullet_spawn(tank_dict):
    global changes
    bullet=pygame.rect.Rect([0,0,6,8])
    speedx=0
    speedy=0
    bullet_dict={'rect':bullet,'angle':tank_dict['angle'],'image':bullet_image,'speedx':speedx,'speedy':speedy}
    rect_helper.rect_change(bullet, tank_dict['angle'] in [0, 180], bullet_image, bullet_original_width, True)
    if bullet_dict['angle']==0:
        bullet.centerx=tank_dict['rect'].centerx
        bullet.bottom = tank_dict['rect'].top
        bullet_dict['speedy']=-3
    if bullet_dict['angle']==180:
        bullet.centerx=tank_dict['rect'].centerx
        bullet.top = tank_dict['rect'].bottom
        bullet_dict['speedy'] = 3
    if bullet_dict['angle']==90:
        bullet.left = tank_dict['rect'].right
        bullet.centery = tank_dict['rect'].centery
        bullet_dict['speedx'] = 3
    if bullet_dict['angle'] == 270:
        bullet.right = tank_dict['rect'].left
        bullet.centery = tank_dict['rect'].centery
        bullet_dict['speedx'] = -3
    bullets.append(bullet_dict)
    changes=True



def map_create():
    karta_def=karta.split('\n')
    for map in range(len(karta_def)):
        type_block_list=karta_def[map]
        for block in type_block_list:

            if type_block_list[int(block)]=='0':
                continue
            if type_block_list[int(block)]=='1':
                block=block_helper.block_create(block_helper.BLOCK_TYPE_BRICK,map_size,int(block),map)
                rects.append(block)


        # if map=='\n':
        #     y += 1
        #     x=0
        # if cycle:
        #     continue
        # if map == '0':
        #     x += 1000 / map_size
        # if map == '1':
        #     block=block_helper.block_create(block_helper.BLOCK_TYPE_BRICK,map_size,5,4)
        #     rects.append(block)
        #     x += 1000 / map_size
        # if map=='2':
        #     # build = True
        #     brick = pygame.rect.Rect([x, y, size_metal, size_metal])
        #     block = {'rect': brick, 'type': 'steel'}
        #     rects.append(block)
        #     # print(brick)
        #     x += 1000 / map_size
        #     cycle = True
        cycle = False

def tank_angle_and_move(angle2,speedx2,speedy2,tank_dict):
    global angle,speedx,speedy,changes
    tank_dict['angle'] = angle2
    tank_dict['speedx'] = speedx2
    tank_dict['speedy'] = speedy2
    rect_helper.rect_change(tank_dict['rect'], tank_dict['angle'] in [0,180], tank_dict["image"], original_width, True)
    changes = True

# def rect_change():

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
        bullets_dict['rect'].x+=bullets_dict['speedx']
        bullets_dict['rect'].y+=bullets_dict['speedy']

    # for line in rects:
    #     if line['rect'].colliderect(tank_dict['rect']):
    #         if tank_dict['rect'].left<line['rect'].right and tank_dict['angle']==270:
    #             tank_dict['rect'].left=line['rect'].right
    #             continue
    #         if tank_dict['rect'].right > line['rect'].left and tank_dict['angle']==90:
    #             tank_dict['rect'].right = line['rect'].left
    #             continue
    #         if tank_dict['rect'].top < line['rect'].bottom and tank_dict['angle']==0:
    #             tank_dict['rect'].top = line['rect'].bottom
    #             continue
    #         if tank_dict['rect'].bottom > line['rect'].top and tank_dict['angle'] == 180:
    #             tank_dict['rect'].bottom = line['rect'].top
    #             continue

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
# karta="""000
# 000
# 000"""
map_size=len(karta.split('\n'))
rects=[]
map_create()

bullet_image=pygame.image.load('sprites/battle_city_items/bullet.png')
bullet_original_width = 60 / map_size

# Подоготовка танка
original_width = 500 / map_size
t1=tank_create(0,0,'player','purple')
t2=tank_create(5,4,'player','white')
t3=tank_create(0,3,'enemy','yellow')
t4=tank_create(1,7,'enemy','green')
tanks=[t1,t2,t3,t4]
bullets=[]
print(t1)




