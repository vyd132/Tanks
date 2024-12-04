import pygame,messenger
shot_sound=pygame.mixer.Sound('sounds/shot.mp3')
tank_died_enemy_sound=pygame.mixer.Sound('sounds/tank_died.mp3')
tank_died_player_sound=pygame.mixer.Sound('sounds/player is shot or the base (eagle) is blown up.mp3')


def sounds(type,who,addons):
    if type=='bullet_spawn':
        shot_sound.play()
    if type=='tank_died' and addons=='enemy':
        tank_died_enemy_sound.play()
    if type=='tank_died' and addons=='player':
        tank_died_player_sound.play()


messenger.add_subs(sounds)