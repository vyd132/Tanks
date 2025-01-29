import pygame,pygame_gui,model_main_menu
from model_main_menu import mananger

def event():
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            exit()
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == model_main_menu.button_play:
            print('work')
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == model_main_menu.button_exit:
            exit()
        mananger.process_events(event)