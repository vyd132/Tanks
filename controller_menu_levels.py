import pygame,pygame_gui,model_menu_levels
from model_menu_levels import mananger

def event():
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            exit()
        model_menu_levels.levels_buttons_check(event)
        mananger.process_events(event)