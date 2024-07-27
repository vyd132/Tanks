import pygame,model
pygame.init()
screen=pygame.display.set_mode([1000,1000])
bullet=pygame.image.load('sprites/battle_city_items/bullet.png')
bullet=pygame.transform.scale(bullet,[6,8])
brick = pygame.image.load('sprites/battle_city_items/block_brick.png')
brick = pygame.transform.scale(brick, [32, 32])

bricks=[]

def view():
    global screen
    screen.fill([0, 0, 0])
    bricks.clear()
    for line in range(0,1000,32):
        bricks.append(brick)
        if len(bricks)==8:
            continue
        screen.blit(brick,[line,500])
        if model.show_rects:
            pygame.draw.rect(screen, [255, 0, 0],[line,500,32,32] , width=1)
    screen.blit(bullet, [model.bullet.left, model.bullet.top])
    if model.show_rects:
        pygame.draw.rect(screen,[255,0,0],model.bullet,width=1)
    pygame.display.flip()
