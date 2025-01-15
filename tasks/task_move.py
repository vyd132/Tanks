import random,pygame,tank_helper

def action_create(task,tank_dict):
    task['range'] = random.randint(100, 100)
    task['start_x'] = tank_dict['rect'].centerx
    task['start_y'] = tank_dict['rect'].centery
    task['turn'] = random.choice(['right', 'left', 'up', 'down'])
    task['action_type'] = 'move'


def action_check(tank_dict,range):
    if tank_dict['task']['turn']=='right':
         return tank_dict['rect'].centerx>=tank_dict['task']['start_x']+range
    elif tank_dict['task']['turn']=='left':
        return tank_dict['rect'].centerx<=tank_dict['task']['start_x']-range
    if tank_dict['task']['turn']=='up':
        return tank_dict['rect'].centery<=tank_dict['task']['start_y']-range
    elif tank_dict['task']['turn']=='down':
        return tank_dict['rect'].centery>=tank_dict['task']['start_y']+range

def action_do(task,tank_dict):
    name = getattr(tank_helper, task['turn'])
    name(tank_dict)