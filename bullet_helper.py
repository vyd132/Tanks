import pygame,rect_helper,block_helper
bullet_image=pygame.image.load('sprites/battle_city_items/bullet.png')

def bullet_fly(bullets_dict,block_list):
    bullets_dict['rect'].x += bullets_dict['speedx']
    bullets_dict['rect'].y += bullets_dict['speedy']
    for block_dict in block_list:
        collide=block_helper.block_check(block_dict,bullets_dict['rect'])
        if collide:
            return True


def bullet_spawn(tank_dict,block_count,bullet_list):
    bullet=pygame.rect.Rect([0,0,6,8])
    speedx=0
    speedy=0
    bullet_dict={'rect':bullet,'angle':tank_dict['angle'],'image':bullet_image,'speedx':speedx,'speedy':speedy}
    rect_helper.rect_change(bullet, tank_dict['angle'] in [0, 180], bullet_image,60/block_count, True)
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
    bullet_list.append(bullet_dict)
    return True