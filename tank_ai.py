import time

import pygame,tank_helper,random
from tasks import task_move,task_wait,task_fire



def comands(tank_dict):
    if tank_dict['type'] != 'enemy':
        return
    task = tank_dict['task']
    if task['action_type'] == 'move':
        task_move_check = task_move.action_check(tank_dict, task['range'])
        if task_move_check:
            random_task(task,tank_dict)
            return
        task_move.action_do(task,tank_dict)
    if task['action_type'] == 'wait':
        if task_wait.action_check(tank_dict):
            task_move.action_create(task,tank_dict)
            return
    if task['action_type'] == 'fire':
        if task_fire.action_check(tank_dict):
            random_task(task,tank_dict)
            return
        task_fire.action_do(tank_dict)



def move_stop(tank_dict):
    if 'task' in tank_dict and tank_dict['task']['action_type']=='move':# and tank_dict['task']['action']:
        task_wait.action_create(tank_dict['task'],tank_dict)

def random_task(task,tank_dict):
    module=random.choice([task_wait,task_move,task_fire])
    module.action_create(task,tank_dict)



