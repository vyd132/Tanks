import time,random

def action_check(tank_dict):
    timer = time.time()
    if timer >= tank_dict['task']['timer']:
        return True


def action_create(task,tank_dict):
    task['timer'] = time.time() + random.randint(0.5, 2)
    task['action_type'] = 'wait'


def action_do():
    pass