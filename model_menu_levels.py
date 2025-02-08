import pygame,pygame_gui

import levels
import model

pygame.init()
mananger=pygame_gui.UIManager((1000,1000),'gui_levels.json')
buttons_list=[]
def levels_buttons_create():
    level_name = 1
    offsets = 50
    button_colx = 4
    button_coly = 3
    button_size = 210
    offsets_buttons = (1000 - button_size * button_colx - offsets * 2) / (button_colx - 1)
    text_sizey = 40
    for line_y in range(button_coly):
        for line_x in range(button_colx):
            level_rect_button = pygame.rect.Rect([offsets+button_size*line_x+offsets_buttons*line_x, 50+button_size*line_y+100*line_y, button_size, button_size])
            button=pygame_gui.elements.UIButton(level_rect_button,'',mananger,object_id=pygame_gui.core.ObjectID('#level_'+str(level_name),'@level_buttons'))
            level_rect_label1=pygame.rect.Rect([offsets+button_size*line_x+offsets_buttons*line_x,level_rect_button.bottom,button_size,text_sizey])
            level_rect_label2 = pygame.rect.Rect(
                [offsets + button_size * line_x + offsets_buttons * line_x, level_rect_button.bottom+40, button_size,
                 text_sizey])
            pygame_gui.elements.UILabel(level_rect_label1,levels.levels_list[level_name-1]['name'].split('\n')[0],mananger,object_id='@level_labels')
            pygame_gui.elements.UILabel(level_rect_label2, levels.levels_list[level_name - 1]['name'].split('\n')[1], mananger,object_id='@level_labels')
            buttons_list.append(button)
            if len(levels.levels_list)==level_name:
                return
            level_name+=1

levels_buttons_create()
def levels_buttons_check(event):
    for button in range(len(buttons_list)):
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == buttons_list[button]:
            levels.level_change(button)
            model.active_screen='game'


