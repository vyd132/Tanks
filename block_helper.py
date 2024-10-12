import pygame
small_block_count=2

BLOCK_TYPE_BRICK=1
BLOCK_TYPE_STEEL=2
brick_image=pygame.image.load('sprites/battle_city_items/block_brick.png')
steel_image=pygame.image.load('sprites/battle_city_items/block_steel.png')
def block_check(block_dict,bullet_rect):
    collidebig = block_dict['final_rect'].colliderect(bullet_rect)
    if not collidebig:
        return
    for block_rect in block_dict['rects']:
        collide=block_rect.colliderect(bullet_rect)
        if collide:
            block_dict['rects'].remove(block_rect)
            return True


def image_block_create(block:dict):
    brick_rect_copy =block['final_rect']
    block_clear = pygame.Surface(block['final_rect'].size)
    image=brick_image if block['type']==BLOCK_TYPE_BRICK else steel_image
    brick = pygame.transform.scale(image, [block['final_rect'].width/small_block_count+1,block['final_rect'].height/small_block_count+1])
    for brick_rect in block['rects']:
        block_clear.blit(brick,[brick_rect.x-brick_rect_copy.x,brick_rect.y-brick_rect_copy.y])
    return block_clear


def block_create(type_of_block:int,mapsize:int,x:int,y:int):
    blocks_list=[]
    block_size=1000 / mapsize
    for blocky in range(small_block_count):
        for blockx in range(small_block_count):

            # print(test_cord)
            x_rect=block_size * x+(block_size/small_block_count*blockx)
            print(x)
            y_rect=block_size * y+(block_size/small_block_count*blocky)
            brick=pygame.rect.Rect([x_rect,y_rect,(block_size)/small_block_count+1,(block_size)/small_block_count+1])
            blocks_list.append(brick)
    block = {
            'rects': blocks_list,
             'type': int(type_of_block),
             'final_rect':pygame.rect.Rect([block_size * x,block_size* y,block_size,block_size])
             }

    return block

