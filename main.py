import view_main
import controller_main_menu
import model,view_game,controller_game,time
import view_main_menu

while True:
    time.sleep(1/60)
    if model.active_screen=='game':
        controller_game.event()
        view_game.view()
    if model.active_screen=='main':
        view_main_menu.view()
        controller_main_menu.event()
