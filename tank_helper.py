import pygame,rect_helper
pygame.init()
font=pygame.font.SysFont('arial',20,True)

def upgrade(tank_dict):
    if tank_dict['lvl']+1==len(tank_dict['costumes']):
        return
    tank_dict['lvl']+=1
    tank_dict['hp']+=1
    lvl_change(tank_dict)

def lvl_change(tank_dict):
    tank_dict["image"] = pygame.image.load(tank_dict['costumes'][tank_dict['lvl']])
    rect_helper.rect_change(tank_dict['rect'], tank_dict['angle'] in [0, 180], tank_dict["image"],
                            tank_dict['original_width'], True)


def downgrade(tank_dict):
    if tank_dict['lvl']==0:
        return
    tank_dict['lvl']-=1
    tank_dict['hp']-=1
    lvl_change(tank_dict)

def view(tank_dict,surface):
    surface.blit(tank_dict['image_view'], tank_dict["rect"])

def debug_view(tank_dict,surface):
    pygame.draw.rect(surface, [255, 255, 0], tank_dict["rect"], width=1)
    text=font.render('lvl: '+str(tank_dict['lvl']),True,[255,0,0])
    surface.blit(text,[tank_dict['rect'].x,tank_dict['rect'].y])
    text = font.render('hp: ' + str(tank_dict['hp']), True, [255, 0, 0])
    surface.blit(text, [tank_dict['rect'].x, tank_dict['rect'].centery])

def hp_change_costume(tank_dict):
    if tank_dict['type']=='player':
        return
    if tank_dict['hp']==2:
        tank_dict['costumes']=costume_list_gen('enemy','yellow')
        tank_dict['image'] = pygame.image.load(tank_dict['costumes'][tank_dict['lvl']])
    if tank_dict['hp'] == 1:
        tank_dict['costumes']=costume_list_gen('enemy', 'white')
        tank_dict['image'] = pygame.image.load(tank_dict['costumes'][tank_dict['lvl']])

def costume_list_gen(type,color):
    tank_list=[]
    for size in range(1,5):
        tank_list.append('sprites/battle_city_tanks/tank_'+type+'_size'+str(size)+'_'+color+'1.png')
    return tank_list

def enemy_param_change(tank_dict,hp):
    if tank_dict['type']=='player':
        return
    tank_dict['hp']=hp

def tank_create(x,y,type,color,map_size,hp,lvl):
    tank = pygame.rect.Rect([0, 0, 0, 0])
    t1 = {
        "rect": tank,
        'angle': 0,
        "speedx": 0,
        "speedy": 0,
        'bullet_speed': 3,
        'bullets_limit':3,
        'my_bullets':0,
        'color':color,
        'type':type,
        'lvl':lvl,
        'original_width':500 / map_size
    }
    t1['costumes'] = costume_list_gen(type, t1['color'])
    t1['image']= pygame.image.load(t1['costumes'][t1['lvl']])
    t1['hp']=t1['lvl']+1
    enemy_param_change(t1,hp)
    hp_change_costume(t1)
    rect_helper.rect_change(t1['rect'], t1['angle'] == 0, t1['image'], t1['original_width'], True)
    tank.centerx = (1000 / map_size) * x + (1000 / map_size) / 2
    tank.centery = 1000 / map_size * y + (1000 / map_size) / 2
    return t1

