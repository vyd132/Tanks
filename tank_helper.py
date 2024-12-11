import pygame,rect_helper

import messenger

pygame.init()
font=pygame.font.SysFont('arial',20,True)



def tank_die(tank_list,tank_dict):
    messenger.broadcast('tank_died',tank_dict,tank_dict['type'])
    tank_list.remove(tank_dict)


def enemy_downgarde(tank_dict,tank_list):
    if tank_dict['hp']<=1:
        tank_die(tank_list,tank_dict)
        return
    tank_dict['hp']-=1
    hp_change_costume(tank_dict)
    tanks_save(tank_dict)

def upgrade(tank_dict):
    if tank_dict['lvl']+1==len(tank_dict['costumes']):
        return
    tank_dict['lvl']+=1
    tank_dict['hp']+=1
    player_lvl_change(tank_dict)
    tanks_save(tank_dict)

def player_lvl_change(tank_dict):
    if tank_dict['type']!='player':
        return
    if tank_dict['lvl']>=1:
        tank_dict['bullet_speed']=6
        tank_dict['bullets_limit'] = 2
    else:
        tank_dict['bullet_speed'] = 2
        tank_dict['bullets_limit'] = 1

    if tank_dict['lvl']==3:
        tank_dict['can_break_metal']=True
    else:
        tank_dict['can_break_metal'] = False
    tank_dict["image"] = pygame.image.load(tank_dict['costumes'][tank_dict['lvl']])
    _tank_rect_change(tank_dict,False)


def right(tank_dict):
    tank_dict['angle'] = 90
    tank_dict['speedx'] = 3
    tank_dict['speedy'] = 0
    _tank_rect_change(tank_dict,True)

def left(tank_dict):
    tank_dict['angle'] = 270
    tank_dict['speedx'] = -3
    tank_dict['speedy'] = 0
    _tank_rect_change(tank_dict,True)

def down(tank_dict):
    tank_dict['angle'] = 180
    tank_dict['speedx'] = 0
    tank_dict['speedy'] = 3
    _tank_rect_change(tank_dict,True)

def up(tank_dict):
    tank_dict['angle'] = 0
    tank_dict['speedx'] = 0
    tank_dict['speedy'] = -3
    _tank_rect_change(tank_dict,True)


def _tank_rect_change(tank_dict,do_tank_save):
    rect_helper.rect_change(tank_dict['rect'], tank_dict['angle'] in [0, 180], tank_dict["image"],
                            tank_dict['original_width'], True)
    if do_tank_save:
        tanks_save(tank_dict)


def pos_change(x,y,tank_dict):
    tank_dict['rect'].centerx = (1000 / tank_dict['block_col']) * x + (1000 / tank_dict['block_col']) / 2
    tank_dict['rect'].centery = 1000 / tank_dict['block_col'] * y + (1000 / tank_dict['block_col']) / 2


def angle_change(tank_dict,angle):
    tank_dict['angle'] = angle
    _tank_rect_change(tank_dict, True)

def bullets_clear(tank_dict):
    tank_dict['my_bullets']=0


def tank_timer(timer,lvl_time):
    pygame.time.set_timer(timer, lvl_time)


def metal_check(tank_dict):
    return tank_dict['can_break_metal']

def downgrade(tank_dict):
    if tank_dict['lvl']==0:
        return
    tank_dict['lvl']-=1
    tank_dict['hp']-=1
    player_lvl_change(tank_dict)
    tanks_save(tank_dict)

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
    if tank_dict['hp']>=3:
        color='purple'
    if tank_dict['hp']==2:
        color='yellow'
    if tank_dict['hp'] == 1:
        color='white'
    tank_dict['costumes'] = costume_list_gen('enemy', color)
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
    if tank_dict['lvl']==3:
        tank_dict['can_break_metal']=True
    else:
        tank_dict['can_break_metal'] = False

def tank_check(tank_dict,bullet_rect,tank_list):
    if tank_dict['rect'].colliderect(bullet_rect):
        enemy_downgarde(tank_dict,tank_list)
        return True



def tanks_save(tank_dict):
    tank = pygame.transform.rotate(tank_dict["image"], -tank_dict["angle"])
    tank = pygame.transform.scale(tank, tank_dict["rect"].size)
    tank_dict['image_view'] = tank

def tank_create(x,y,type,color,map_size,hp,lvl):
    tank = pygame.rect.Rect([0, 0, 0, 0])
    t1 = {
        "rect": tank,
        'angle': 0,
        "speedx": 0,
        "speedy": 0,
        'bullet_speed': 2,
        'bullets_limit':1,
        'my_bullets':0,
        'color':color,
        'type':type,
        'lvl':lvl,
        'original_width':500 / map_size,
        'can_break_metal':False,
        'block_col':map_size
    }
    t1['costumes'] = costume_list_gen(type, t1['color'])
    t1['image']= pygame.image.load(t1['costumes'][t1['lvl']])
    t1['hp']=t1['lvl']+1
    enemy_param_change(t1,hp)
    hp_change_costume(t1)
    player_lvl_change(t1)
    _tank_rect_change(t1,True)
    pos_change(x,y,t1)
    return t1

