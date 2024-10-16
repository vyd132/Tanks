import pygame,rect_helper

def change_costume(tank_dict,original_width):
    tank_dict["image"]=pygame.image.load(tank_dict['costumes'][tank_dict['costume_number']])
    rect_helper.rect_change(tank_dict['rect'], tank_dict['angle'] in [0,180], tank_dict["image"], original_width, True)
    tank_dict['costume_number']+=1
    if tank_dict['costume_number']==len(tank_dict['costumes']):
        tank_dict['costume_number']=0

def costume_list_gen(type,color):
    tank_list=[]
    for size in range(1,5):
        tank_list.append('sprites/battle_city_tanks/tank_'+type+'_size'+str(size)+'_'+color+'1.png')
    return tank_list

def tank_create(x,y,type,color,map_size,original_width):
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
        "speedy": 0,
        'bullet_speed': 3,
        'hp':3,
        'bullets_limit':3,
        'my_bullets':0
    }
    rect_helper.rect_change(t1['rect'], t1['angle'] == 0, t1['image'], original_width, True)
    tank.centerx = (1000 / map_size) * x + (1000 / map_size) / 2
    tank.centery = 1000 / map_size * y + (1000 / map_size) / 2
    return t1