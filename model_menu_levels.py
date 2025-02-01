import pygame,pygame_gui

pygame.init()
mananger=pygame_gui.UIManager((1000,1000),'gui_levels.json')
level1=pygame.rect.Rect([50,50,210,210])
button_level1=pygame_gui.elements.UIButton(level1,'',mananger,object_id='#level_1')