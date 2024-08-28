import pygame,model

event_type=pygame.event.custom_type()


def event():
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            model.show_rects=not model.show_rects
        # if event.type==pygame.MOUSEBUTTONDOWN:
        #     model.click_check(event.pos)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            model.show_image=not model.show_image
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            model.angle_and_move(0,0,-0,'up and down')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            model.angle_and_move(90,0,0,'left and right')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            model.angle_and_move(180,0,0,'up and down')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            model.angle_and_move(270,-0,0,'left and right')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            model.change_costume()