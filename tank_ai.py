import time

import pygame,tank_helper,random

def tank_wait_check(tank_dict):
    timer=time.time()
    if timer>=tank_dict['task']['timer']:
        tank_dict['task']['action'] = False
        tank_dict['task']['action_type'] = 'move'

def comands(tank_dict):
    if tank_dict['type'] != 'enemy':
        return
    task = tank_dict['task']
    if not task['action'] and task['action_type'] == 'move':
        task['range'] = random.randint(100, 100)
        task['action'] = True
        task['start_x'] = tank_dict['rect'].centerx
        task['start_y'] = tank_dict['rect'].centery
        task['turn']=random.choice(['right','left','up','down'])
    elif not task['action'] and task['action_type'] == 'wait':
        task['timer']=time.time()+random.randint(1,6)
        task['action'] = True
    if task['action_type'] == 'move':
        task_move_check = cord_check(tank_dict, task['range'])
        if task_move_check:
            task['action'] = False
            task['action_type'] = 'wait'
            return
        name=getattr(tank_helper,task['turn'])
        name(tank_dict)
    if task['action_type'] == 'wait':
        tank_wait_check(tank_dict)

def cord_check(tank_dict,range):
    if tank_dict['task']['turn']=='right':
         return tank_dict['rect'].centerx>=tank_dict['task']['start_x']+range
    elif tank_dict['task']['turn']=='left':
        return tank_dict['rect'].centerx<=tank_dict['task']['start_x']-range
    if tank_dict['task']['turn']=='up':
        return tank_dict['rect'].centery<=tank_dict['task']['start_y']-range
    elif tank_dict['task']['turn']=='down':
        return tank_dict['rect'].centery>=tank_dict['task']['start_y']+range

def wall_change(tank_dict):
    if 'task' in tank_dict and tank_dict['task']['action_type']=='move':# and tank_dict['task']['action']:
        tank_dict['task']['action'] = False
        tank_dict['task']['action_type'] = 'wait'





