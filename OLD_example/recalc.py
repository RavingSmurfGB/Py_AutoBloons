import sys
from time import sleep
import pyautogui
from button_positions import *

my_res = (2560, 1440)
target_res = tuple(pyautogui.size())
# target_res = (1920, 1080)

def recalc(start_res:tuple, target_res:tuple, position:tuple):
    sx, sy = start_res
    tx, ty = target_res
    
    spx, spy = position

    mx, my = (tx/sx, ty/sy)

    epx = mx*spx
    epy = my*spy

    return (int(epx),int(epy))

MAP_DIFFICULTYS = [recalc(my_res, target_res, pos) for pos in MAP_DIFFICULTYS]
MAPS = [recalc(my_res, target_res, pos) for pos in MAPS]
DIFFICULTYS = [recalc(my_res, target_res, pos) for pos in DIFFICULTYS]
MODES = [recalc(my_res, target_res, pos) for pos in MODES]

HOME_PLAY_BUTTON = recalc(my_res, target_res, HOME_PLAY_BUTTON)
BACK_TO_HOME = recalc(my_res, target_res, BACK_TO_HOME)
NEXT = recalc(my_res, target_res, NEXT)
WIN_COORDINATE = recalc(my_res, target_res, WIN_COORDINATE)
OVERWRITE_SAVE = recalc(my_res, target_res, OVERWRITE_SAVE)

COLLECT_BUTTON = recalc(my_res, target_res, COLLECT_BUTTON)
COLLECT_LEFT = recalc(my_res, target_res, COLLECT_LEFT)
COLLECT_RIGHT = recalc(my_res, target_res, COLLECT_RIGHT)
COLLECT_CONTINUE = recalc(my_res, target_res, COLLECT_CONTINUE)

LEVEL_UP_COORD = recalc(my_res, target_res, LEVEL_UP_COORD)

print(MAP_DIFFICULTYS, MAPS, DIFFICULTYS, MODES)