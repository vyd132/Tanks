import pygame


BLOCK_TYPE_BRICK=1
BLOCK_TYPE_STEEL=2

def block_create(type_of_block:int,mapsize:int,x:int,y:int):
    blocks_list=[]
    for blocky in range(2):
        for blockx in range(2):

            # print(test_cord)
            x_rect=1000 / mapsize * x+(500 / mapsize*blockx)
            print(x)
            y_rect=1000 / mapsize * y+(500 / mapsize*blocky)
            brick=pygame.rect.Rect([x_rect,y_rect,(1000 / mapsize)/2,(1000 / mapsize)/2])
            blocks_list.append(brick)
            x_rect=0
            y_rect=0
    block = {'rects': blocks_list, 'type': type_of_block}

    return block

