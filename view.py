import pygame,model
pygame.init()
screen=pygame.display.set_mode([1000,1000])
brick=pygame.image.load('sprites/battle_city_items/block_brick.png')
brick=pygame.transform.scale(brick,[32,32])
bullet=pygame.image.load('sprites/battle_city_items/bullet.png')
bullet=pygame.transform.scale(bullet,[6,8])

def view():
    global screen
    screen.fill([0, 0, 0])
    pygame.display.flip()
