import random

import pygame

cycle=False
show_rects=False
show_image=True
build=True
changes=False
karta="""00011220
01222100
12000111
02211012
02101021
01212000
11112220
20221100"""
# karta="""0110
# 0010
# 2020
# 1000"""
angle=0
speedx=0
speedy=0
rects=[]
map_size=len(karta.split('\n'))
# tank_image=pygame.image.load(random.choice(['sprites/battle_city_tanks/tank_player_size1_green1.png','sprites/battle_city_tanks/tank_player_size2_green1.png','sprites/battle_city_tanks/tank_player_size3_green1.png','sprites/battle_city_tanks/tank_player_size4_green1.png']))
tank_image=pygame.image.load('sprites/battle_city_tanks/tank_player_size1_green1.png')
w=tank_image.get_width()
h=tank_image.get_height()
tank=pygame.rect.Rect([400,540,500 / map_size,(h*500 / map_size)/w])
width2 = tank.w
heith2=tank.h
print(tank)
x=0
y = 0
rotate='up and down'
costume_number=0
w2=500 / map_size
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
    global angle,speedx,speedy,width2,heith2,rotate
    angle = angle2
    speedx = speedx2
    speedy = speedy2
    rotate=rotate_param
    if rotate_param=='left and right':
        tank.w = heith2
        tank.h = width2
    if rotate_param=='up and down':
        tank.w = width2
        tank.h = heith2

def change_costume():
    global tank_image,costume_number,changes,w,h,tank,width2,heith2
    tanks=['sprites/battle_city_tanks/tank_player_size1_green1.png','sprites/battle_city_tanks/tank_player_size2_green1.png','sprites/battle_city_tanks/tank_player_size3_green1.png','sprites/battle_city_tanks/tank_player_size4_green1.png']
    tank_image=pygame.image.load(tanks[0+costume_number])
    w = tank_image.get_width()
    h = tank_image.get_height()
    x=tank.x
    y=tank.y
    tank=None
    if rotate=='up and down':
        tank = pygame.rect.Rect([x, y, 500 / map_size, (h * 500 / map_size) / w])
    elif rotate=='left and right':
        tank = pygame.rect.Rect([x, y,(h * 500 / map_size) / w, 500 / map_size ])
    width2 = tank.w
    heith2 = tank.h
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




