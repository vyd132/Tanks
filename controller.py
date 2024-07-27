import pygame,model

event_type=pygame.event.custom_type()


def event():
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            model.show_rects=not model.show_rects
        if event.type==pygame.MOUSEBUTTONDOWN:
            model.click_check(event.pos)