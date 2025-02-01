import pygame,view_main
from model_menu_levels import mananger

def view():
    mananger.update(1/60)
    view_main.screen.fill([0, 0, 0])
    mananger.draw_ui(view_main.screen)
    pygame.display.flip()