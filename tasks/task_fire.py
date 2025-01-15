import bullet_helper,model

def action_create(task,tank_dict):
    task['action_type'] = 'fire'
    task['fire']=False

def action_check(tank_dict):
    return tank_dict['task']['fire']


def action_do(tank_dict):
    bullet_helper.bullet_spawn(tank_dict, model.map_size, model.bullets)
    tank_dict['task']['fire'] = True