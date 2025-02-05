import pygame,pygame_gui

pygame.init()
mananger=pygame_gui.UIManager((1000,1000),'gui_levels.json')
level1=pygame.rect.Rect([50,50,210,210])
button_level1=pygame_gui.elements.UIButton(level1,'',mananger,object_id='#level_1')
level_name=1
offsets=50
button_colx=4
button_coly=3
button_size=210
offsets_buttons=(1000-button_size*button_colx-offsets*2)/(button_colx-1)
text_sizey=80
for line_y in range(button_coly):
    for line_x in range(button_colx):
        level_rect_button = pygame.rect.Rect([offsets+button_size*line_x+offsets_buttons*line_x, 50+button_size*line_y+100*line_y, button_size, button_size])
        button_level=pygame_gui.elements.UIButton(level_rect_button,'',mananger,object_id=pygame_gui.core.ObjectID('#level_'+str(level_name),'@level_buttons'))
        level_rect_label=pygame.rect.Rect([offsets+button_size*line_x+offsets_buttons*line_x,level_rect_button.bottom,button_size,text_sizey])
        pygame_gui.elements.UILabel(level_rect_label,'test',mananger,object_id='@level_labels')
        level_name+=1

