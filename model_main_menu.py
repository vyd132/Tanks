import pygame,pygame_gui

pygame.init()
mananger=pygame_gui.UIManager((1000,1000),'gui.json')
button_rect=pygame.rect.Rect([0,-50,400,50])
button_rect_exit=pygame.rect.Rect([0,50,400,50])
button_play=pygame_gui.elements.UIButton(button_rect,'button',mananger,anchors={'center':'center'},object_id='#level_button')
print(button_rect)
button_exit=pygame_gui.elements.UIButton(button_rect_exit,'exit',mananger,anchors={'center':'center'},object_id='#exit_button')