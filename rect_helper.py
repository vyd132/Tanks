import pygame

def rect_change(rect,vertical,image,vertical_size_width,vertical_image):
    w = image.get_width()
    h = image.get_height()
    if vertical_image:
        if vertical:
            rect.w = vertical_size_width
            rect.h=(h * vertical_size_width) / w
            return
        rect.w = (h * vertical_size_width) / w
        rect.h = vertical_size_width
        return
    if vertical:
        rect.w = vertical_size_width
        rect.h = (w * vertical_size_width) / h
        return
    rect.w = (w * vertical_size_width) / h
    rect.h = vertical_size_width

# rotate=False
#     test=pygame.rect.Rect([400,540,60,60])
#     tank2=pygame.transform.rotate(model.tank_image, 90)
#     rect_helper.rect_change(test,rotate,tank2,60,False)
#     tank2 = pygame.transform.scale(tank2, test.size)
#     screen.blit(tank2, test)
#     pygame.draw.rect(screen, [255, 255, 0], test, width=1)
#
#
#
#     rotate = True
#     test = pygame.rect.Rect([550, 540, 60, 60])
#     tank2 = pygame.transform.rotate(model.tank_image, 0)
#     rect_helper.rect_change(test, rotate, tank2, 60, True)
#     tank2 = pygame.transform.scale(tank2, test.size)
#     screen.blit(tank2, test)
#     pygame.draw.rect(screen, [255, 255, 0], test, width=1)
#
#     rotate = False
#     test = pygame.rect.Rect([660, 540, 60, 60])
#     tank2 = pygame.transform.rotate(model.tank_image, 0)
#     rect_helper.rect_change(test, rotate, tank2, 60, True)
#     tank2 = pygame.transform.scale(tank2, test.size)
#     screen.blit(tank2, test)
#     pygame.draw.rect(screen, [255, 255, 0], test, width=1)
#
#
#
#     rotate = True
#     test = pygame.rect.Rect([750, 540, 60, 60])
#     tank2 = pygame.transform.rotate(model.tank_image, 90)
#     rect_helper.rect_change(test, rotate, tank2, 60, False)
#     tank2 = pygame.transform.scale(tank2, test.size)
#     screen.blit(tank2, test)
#     pygame.draw.rect(screen, [255, 255, 0], test, width=1)
#     print(test.size)