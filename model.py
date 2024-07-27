import pygame

rects=[]



bullet=pygame.rect.Rect([500,-50,6,8])
brick=pygame.rect.Rect([0,500,32,32])
show_rects=False
collide=False

def rect_create(x,y,h,w):
    brick = pygame.rect.Rect([x, y, w, h])
    rects.append(brick)
    return brick

def click_check(cord):
    for line in rects:
        res=line.collidepoint(cord)
        if res:
            number=rects.index(line)
            rects.remove(line)
            print('work')

def model():
    global collide
    rects.clear()
    bullet.bottom+=3
    for line in range(0, 1000, 32):
        if len(rects)==7:
            continue
        rect_create(line,500,32,32)
    for line in rects:
        if bullet.colliderect(line):
            print('hi')





