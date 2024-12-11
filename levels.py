import messenger,pygame

current_level=1
levels_list=[]
level1={'map':"""00011220
01222100
12000111
02211012
02101021
01212000
11112220
20221100""",
        'x':0,
        'y':0,
        't_angle':180,
        'enemy_pos':[{'x':0,"y":7,'time':1000},{'x':7,"y":7,'time':2000},{'x':2,"y":7,'time':3000}]
        }
level2={'map':"""00122100
00122100
00122100
00122100
00122100
00122100
00122100
00122100""",
        'x':7,
        'y': 0,
        't_angle':270,
        'enemy_pos':[{'x':0,"y":7,'time':1000},{'x':7,"y":7,'time':2000},{'x':1,"y":7,'time':3000}]

}
levels_list.append(level1)
levels_list.append(level2)

def level_change(level_number):
    global current_level
    current_level=level_number
    messenger.broadcast('level_changed',levels_list[current_level-1])



