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

def angle_and_move(angle2,speedx2,speedy2,rotate_param):
    global angle,speedx,speedy,original_width,original_height,rotate,changes
    angle = angle2
    speedx = speedx2
    speedy = speedy2
    rotate=rotate_param
    rect_helper.rect_change(tank, rotate == 'up and down', tank_image, original_width, True)
    changes = True

# def rect_change():

def change_costume():
    global tank_image,costume_number,changes,w,h,tank,original_width,original_height
    tank_image=pygame.image.load(tanks[0+costume_number])
    rect_helper.rect_change(tank, rotate =='up and down', tank_image, original_width, True)
    costume_number+=1
    changes = True
    if costume_number==len(tanks):
        costume_number=0

def model():
    global speedx,speedy,changes
    changes=False
    tank.x+=speedx
    tank.y+=speedy
    speedx=0
    speedy=0
    for line in rects:
        if line['rect'].colliderect(tank):
            if tank.left<line['rect'].right and angle==270:
                tank.left=line['rect'].right
                continue
            if tank.right > line['rect'].left and angle==90:
                tank.right = line['rect'].left
                continue
            if tank.top < line['rect'].bottom and angle==0:
                tank.top = line['rect'].bottom
                continue
            if tank.bottom > line['rect'].top and angle == 180:
                tank.bottom = line['rect'].top
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


#Подоготовка танка
angle=0
if angle==90 or angle==270:
    rotate='left and right'
else:
    rotate = 'up and down'

speedx=0
speedy=0

tanks=['sprites/battle_city_tanks/tank_player_size1_green1.png','sprites/battle_city_tanks/tank_player_size2_green1.png','sprites/battle_city_tanks/tank_player_size3_green1.png','sprites/battle_city_tanks/tank_player_size4_green1.png']
tank_image=pygame.image.load(tanks[0])
costume_number=0

w=tank_image.get_width()
h=tank_image.get_height()
tank=pygame.rect.Rect([400,540,0,0])
original_width = 500 / map_size
rect_helper.rect_change(tank,rotate=="up and down",tank_image,original_width,True)



