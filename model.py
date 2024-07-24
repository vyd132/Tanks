import pygame

bullet=pygame.rect.Rect([500,-50,6,8])
brick=pygame.rect.Rect([0,500,32,32])
show_rects=False
collide=False
def model():
    global collide
    bullet.bottom+=3
    if brick.colliderect(bullet):
        collide=True



