import pygame

def rect_change(rect:pygame.Rect,vertical:bool,image:pygame.Surface,vertical_size_width:int,vertical_image:bool):
    """
    Деф для изменения прямоугольника rect. По направлености vertical. По картинке image и vertical_image
    :param rect: Прямоугольника rect у которого изменяется ширина и высота
    :param vertical: Если вверх либо вниз то True, если вправо либо влево False
    :param image: Изменяет ширину и высоту прямоугольника rect по пропорциям картинки image
    :param vertical_size_width: Ширина итогового прямоугольника rect если он стоит вертикально
    :param vertical_image: Если объект направлен вверх либо вниз True, если вправо либо влево False
    :return:
    """
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