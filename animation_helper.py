import pygame,random
anim_list=['sprites/battle_city_items/effect_explosion1.png',
           'sprites/battle_city_items/effect_explosion2.png',
           'sprites/battle_city_items/effect_explosion3.png']

def image_create(map_size,size,anim_list_new):
    for i in anim_list:
        effect = pygame.image.load(i)
        effect = pygame.transform.scale(effect, [size/map_size, size/map_size])
        anim_list_new.append(effect)

def create(effect_list,x,y,list,loops):
    anim_dict={'image_list':list,'costume_number':0,'change':True,'x':x,'y':y,'cycle':0,'loops':loops}
    anim_save(anim_dict)
    anim_dict['size']=anim_dict['image_new'].get_width()
    effect_list.append(anim_dict)

def view(anim_dict,surface):
    surface.blit(anim_dict['image_new'],[anim_dict['x']-anim_dict['size']/2, anim_dict['y']-anim_dict['size']/2])


def anim_change(anim_dict,effect_list):
    if anim_dict['cycle']==anim_dict['loops']:
        effect_list.remove(anim_dict)
    if anim_dict['costume_number'] == 0:
        anim_dict['change'] = True
        anim_dict['cycle']+=1
    if anim_dict['costume_number'] == 2:
        anim_dict['change'] = False
        anim_dict['cycle'] += 1
    if anim_dict['change']:
        anim_dict['costume_number'] += 1
    else:
        anim_dict['costume_number'] -= 1
    anim_save(anim_dict)

def anim_save(anim_dict):
    anim_dict['image_new']=anim_dict['image_list'][anim_dict['costume_number']]