import pygame,tank_helper,random

def comands(tank_dict):
    if tank_dict['type'] != 'enemy':
        return
    task = tank_dict['task']

    if not task['action'] and task['action_type'] == 'move':
        task['range'] = random.randint(5, 20)
        task['action'] = True
        task['start_x'] = tank_dict['rect'].centerx
        task['start_y'] = tank_dict['rect'].centery
        task['turn']=random.choice(['right','left','up','down'])
    elif not task['action'] and task['action_type'] == 'wait':
        return
    if task['action_type'] == 'move':
        task_move_check = cord_check(tank_dict, task['range'])
        if task_move_check:
            task['action'] = False
            task['action_type'] = 'wait'
            print('finish')
            return
        name=getattr(tank_helper,task['turn'])
        name(tank_dict)
    if task['action_type'] == 'wait':
        return

def cord_check(tank_dict,range):
    if tank_dict['task']['turn']=='right':
         return tank_dict['rect'].centerx>=tank_dict['task']['start_x']+range
    elif tank_dict['task']['turn']=='left':
        return tank_dict['rect'].centerx<=tank_dict['task']['start_x']-range

    if tank_dict['task']['turn']=='up':
        return tank_dict['rect'].centery<=tank_dict['task']['start_y']-range
    elif tank_dict['task']['turn']=='down':
        return tank_dict['rect'].centery>=tank_dict['task']['start_y']+range