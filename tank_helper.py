import pygame,rect_helper
pygame.init()
font=pygame.font.SysFont('arial',20,True)
def change_costume(tank_dict,original_width):
    if tank_dict['lvl']+1==len(tank_dict['costumes']):
        return
    tank_dict['lvl']+=1
    tank_dict['hp']+=1
    tank_dict["image"]=pygame.image.load(tank_dict['costumes'][tank_dict['lvl']])
    rect_helper.rect_change(tank_dict['rect'], tank_dict['angle'] in [0,180], tank_dict["image"], original_width, True)


def view(tank_dict,surface):
    surface.blit(tank_dict['image_view'], tank_dict["rect"])

def debug_view(tank_dict,surface):
    pygame.draw.rect(surface, [255, 255, 0], tank_dict["rect"], width=1)
    text=font.render('lvl: '+str(tank_dict['lvl']),True,[255,0,0])
    surface.blit(text,[tank_dict['rect'].x,tank_dict['rect'].y])
    text = font.render('hp: ' + str(tank_dict['hp']), True, [255, 0, 0])
    surface.blit(text, [tank_dict['rect'].x, tank_dict['rect'].centery])

# def hp_change_costume(tank_dict):
#     if tank_dict['hp']==2:
#         tank_dict['costumes']=costume_list_gen('player','yellow')
#         tank_dict['image'] = pygame.image.load(tank_dict['costumes'][0])
#     if tank_dict['hp'] == 1:
#         tank_dict['costumes']=costume_list_gen('player', 'white')
#         tank_dict['image'] = pygame.image.load(tank_dict['costumes'][0])

def costume_list_gen(type,color):
    tank_list=[]
    for size in range(1,5):
        tank_list.append('sprites/battle_city_tanks/tank_'+type+'_size'+str(size)+'_'+color+'1.png')
    return tank_list

def tank_create(x,y,type,color,map_size,original_width):
    tank = pygame.rect.Rect([0, 0, 0, 0])
    t1 = {
        "rect": tank,
        'angle': 0,
        "speedx": 0,
        "speedy": 0,
        'bullet_speed': 3,
        'hp':1,
        'bullets_limit':3,
        'my_bullets':0,
        'color':color,
        'type':type,
        'lvl':0
    }
    t1['costumes'] = costume_list_gen(type, t1['color'])
    t1['image']= pygame.image.load(t1['costumes'][0])
    rect_helper.rect_change(t1['rect'], t1['angle'] == 0, t1['image'], original_width, True)
    tank.centerx = (1000 / map_size) * x + (1000 / map_size) / 2
    tank.centery = 1000 / map_size * y + (1000 / map_size) / 2
    return t1