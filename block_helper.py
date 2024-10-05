import pygame


BLOCK_TYPE_BRICK=1
BLOCK_TYPE_STEEL=2
brick_image=pygame.image.load('sprites/battle_city_items/block_brick.png')
def image_block_create(block:dict):
    for brick_rect in block['rects']:
        block_clear = pygame.Surface([brick_rect.width*2, brick_rect.height*2])
        brick=pygame.transform.scale(brick_image,brick_rect.size)
        block_clear.blit(brick,[brick_rect.x,brick_rect.y])
        pygame.image.save(block_clear,'block_clear.png')
    return block_clear


def block_create(type_of_block:int,mapsize:int,x:int,y:int):
    blocks_list=[]
    block_size=1000 / mapsize
    for blocky in range(2):
        for blockx in range(2):

            # print(test_cord)
            x_rect=block_size * x+(block_size/2*blockx)
            print(x)
            y_rect=block_size * y+(block_size/2*blocky)
            brick=pygame.rect.Rect([x_rect,y_rect,(block_size)/2,(block_size)/2])
            blocks_list.append(brick)
    block = {
            'rects': blocks_list,
             'type': type_of_block,
             'final_rect':pygame.rect.Rect([block_size * x,block_size* y,block_size,block_size])
             }

    return block

