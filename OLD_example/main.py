import pyautogui
from map import Map
from recalc import *
from data_handler import Handler
import time
from threading import Thread
import logger

MODE = "SINGLE_MAP"

Logger = logger.Logger()

t1 = None
src_path = "./data/src/menu"
data_handler = Handler("./data/maps")
map_data = data_handler.read_data("dark_castle.txt")
game_plan = map_data[7:]

game_map = Map(map_data[0], MAP_DIFFICULTYS[int(map_data[1])-1], int(map_data[2]), MAPS[int(map_data[3])-1], DIFFICULTYS[int(map_data[4])], MODES[int(map_data[5])], tuple([int(x) for x in map_data[6].split()])) # maybe last value broken
completed_rounds = 0

def check_win():
    win = False
    while win == False:
        locate = pyautogui.pixel(WIN_COORDINATE[0],WIN_COORDINATE[1])
        if locate == (65, 65, 65):
            win == True
            pyautogui.click(NEXT)
            time.sleep(0.5)
            restart()
        time.sleep(1)

def restart_map():
        Logger.log(f"Run again", "YELLOW")
        pyautogui.click(FREE_PLAY)
        time.sleep(1)
        pyautogui.click(FREE_PLAY_OK)
        time.sleep(1)

        pyautogui.press("ESC")
        time.sleep(0.2)
        pyautogui.click(RESTART_GAME)
        
        time.sleep(0.2)
        pyautogui.click(RESTART_SUBMIT)
        
        time.sleep(3)
        game_plan.play(game_plan)
        check_win()

def check_level_up():
    while True:
        levelup = pyautogui.pixel(LEVEL_UP_COORD[0], LEVEL_UP_COORD[1])
        time.sleep(1)
        if levelup == (163, 81, 33):
            Logger.log("Level Up", "RED")
            pyautogui.click()
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.press("SPACE")

def check_collect():
    collect = pyautogui.pixel(COLLECT_BUTTON[0], COLLECT_BUTTON[1])
    if collect == (104, 229, 0):
        pyautogui.click(COLLECT_BUTTON)
        time.sleep(3)

        pyautogui.click(COLLECT_LEFT)
        time.sleep(1)
        pyautogui.click()
        time.sleep(0.2)

        time.sleep(1)
        pyautogui.click(COLLECT_RIGHT)
        time.sleep(1)
        pyautogui.click()
        time.sleep(0.2)

        time.sleep(1)
        pyautogui.click(COLLECT_CONTINUE)

        time.sleep(0.2)
        pyautogui.press("ESC")

def run_map_again():
    global completed_rounds
    completed_rounds += 1
    Logger.log(f"Rounds completed: {completed_rounds} Cash generated: {completed_rounds*60}", "RED")
    
def restart():
    global completed_rounds
    completed_rounds += 1
    Logger.log(f"Rounds completed: {completed_rounds} Cash generated: {completed_rounds*60}", "RED")
    if MODE == "SINGLE_MAP":
        restart_map()
    else:
        pyautogui.click(BACK_TO_HOME)
        time.sleep(1)
        check_collect()
        main_loop()

def main_loop():
    game_map.select()    
    time.sleep(5)
    game_map.play(game_plan)

    check_win()

level_check_thread = Thread(target=check_level_up, daemon=True)
level_check_thread.start()
main_loop()

