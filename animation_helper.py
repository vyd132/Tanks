import pygame,random
anim_list=['sprites/battle_city_items/effect_explosion1.png',
           'sprites/battle_city_items/effect_explosion2.png',
           'sprites/battle_city_items/effect_explosion3.png']
anim_list_dict = []
for i in anim_list:
    effect = pygame.image.load(i)
    effect = pygame.transform.scale(effect, [100, 100])
    print(1)
    anim_list_dict.append(effect)

def create(effect_list,x,y):
    anim_dict={'image_list':anim_list_dict,'costume_number':0,'change':True,'x':x,'y':y}
    anim_save(anim_dict)
    effect_list.append(anim_dict)

def view(anim_dict,surface):
    surface.blit(anim_dict['image_new'],[anim_dict['x'], anim_dict['y']])


def anim_change(anim_dict):
    if anim_dict['costume_number'] == 0:
        anim_dict['change'] = True
    if anim_dict['costume_number'] == 2:
        anim_dict['change'] = False
    if anim_dict['change']:
        anim_dict['costume_number'] += 1
    else:
        anim_dict['costume_number'] -= 1
    anim_save(anim_dict)

def anim_save(anim_dict):
    anim_dict['image_new']=anim_dict['image_list'][anim_dict['costume_number']]