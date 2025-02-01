import pygame,pygame_gui

pygame.init()
mananger=pygame_gui.UIManager((1000,1000), 'gui_main_menu.json')
button_rect=pygame.rect.Rect([0,-50,400,50])
button_rect_exit=pygame.rect.Rect([0,50,400,50])
button_play=pygame_gui.elements.UIButton(button_rect,'LEVELS',mananger,anchors={'center':'center'},object_id=pygame_gui.core.ObjectID("#level_button",'@my_buttons'), )
print(button_rect)
button_exit=pygame_gui.elements.UIButton(button_rect_exit,'EXIT',mananger,anchors={'center':'center'},object_id=pygame_gui.core.ObjectID('#exit_button','@my_buttons'))
