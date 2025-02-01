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
        'enemy_pos':[{'x':0,"y":7,'time':5000,'tanks_list':[],'sleep':3000,'wave_start':False},
                     # {'x':7,"y":7,'time':2000},{'x':2,"y":7,'time':3000}]
        ]
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
        'enemy_pos':[{'x':0,"y":7,'time':1000,'tanks_list':[0,3,2,1,1,2,3],'sleep':3000,'wave_start':False},
                     {'x':7,"y":7,'time':2000,'tanks_list':[2,3,1,1,0,0],'sleep':10000,'wave_start':False},
                     {'x':1,"y":7,'time':3000,'tanks_list':[],'sleep':5000,'wave_start':False}]

}
levels_list.append(level1)
levels_list.append(level2)

def level_change(level_number):
    global current_level
    current_level=level_number
    messenger.broadcast('level_changed',levels_list[current_level-1])



