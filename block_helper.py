import pygame

BLOCK_TYPE_BRICK=1
BLOCK_TYPE_STEEL=2

def block_create(type_of_block:int,size_of_block:int):
    blocks_list=[]
    for blocky in range(2):
        for blockx in range(2):
            brick=pygame.rect.Rect([(blockx+1)*size_of_block/4,(blocky+1)*size_of_block,size_of_block,size_of_block])
            blocks_list.append(brick)
    block = {'rects': blocks_list, 'type': type_of_block}
    return block