import pygame,model

pygame.key.set_repeat(100)

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
            model.tank_angle_and_move(0,0,-3,model.t1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            model.tank_angle_and_move(90,3,0,model.t1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            model.tank_angle_and_move(180,0,3,model.t1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            model.tank_angle_and_move(270,-3,0,model.t1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            model.change_costume(model.t1)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            model.bullet_spawn(model.t1)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            model.tank_angle_and_move(0,0,-3,model.t2)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            model.tank_angle_and_move(90,3,0,model.t2)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            model.tank_angle_and_move(180,0,3,model.t2)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            model.tank_angle_and_move(270,-3,0,model.t2)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            model.change_costume(model.t2)