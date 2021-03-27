import pyautogui
from time import sleep
from recalc import HOME_PLAY_BUTTON, MAP_DIFFICULTYS, DIFFICULTYS, MODES, OVERWRITE_SAVE
from button_positions import *
from logger import Logger
from monkeys import monkeys, upgrades, SELL, CHANGE_TARGETING, CHANGE_TARGETING_REVERSE, PLAY
from threading import Thread
from recalc import recalc, my_res, target_res


Logger = Logger()

class Map():
    def __init__(self, map_name, map_difficulty, map_site, map_place, difficulty, mode, res):
        self.map_name = map_name
        self.map_difficulty = map_difficulty
        self.map_site = map_site
        self.map_place = map_place
        self.difficulty = difficulty
        self.mode = mode
        self.res = res

    def select(self):
        time_to_home = 5
        Logger.log(f"Open home screen - {time_to_home} sec", "YELLOW")
        sleep(time_to_home)

        x, y = HOME_PLAY_BUTTON
        pyautogui.click(x, y)

        delay = 0.3
        for x in range(self.map_site):
            sleep(delay)
            x, y = self.map_difficulty
            pyautogui.click(x, y)
        
        sleep(delay)
        pyautogui.click(self.map_place)

        sleep(delay)
        pyautogui.click(self.difficulty)

        sleep(delay)
        pyautogui.click(self.mode)
        
        sleep(delay)
        pyautogui.click(OVERWRITE_SAVE)

    def restart_map(self):
        Logger.log(f"Run again", "YELLOW")
        pyautogui.click(FREE_PLAY)
        sleep(1)
        pyautogui.click(FREE_PLAY_OK)
        sleep(1)

        pyautogui.press("ESC")
        sleep(0.2)
        pyautogui.click(RESTART_GAME)
        
        sleep(0.2)
        pyautogui.click(RESTART_SUBMIT)
        
        sleep(3)
        self.play(game_plan)

    def place_monkey(self, key:str, pos:tuple, time_between:int=0.2): # time between maybe to 0?
        pyautogui.press(key)
        pyautogui.moveTo(pos[0], pos[1])
        sleep(time_between)
        pyautogui.click()

    def upgrade_monkey(self, pos:tuple, path):
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.click()
        pyautogui.press(upgrades[path])
        pyautogui.press("ESC")

    def sell_monkey(self, pos:tuple):
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.click()
        pyautogui.press(SELL)

    def change_target(self, pos:tuple, direction:int):
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.click()
        if direction == 1:
            pyautogui.press(CHANGE_TARGETING)
        else:
            pyautogui.hotkey(CHANGE_TARGETING_REVERSE[0], CHANGE_TARGETING_REVERSE[1])
        pyautogui.press("ESC")

    def play(self, game_plan):
        data = []
        for r in game_plan:
            data.append(r.split())
        
        for r in data:
            key = r[0].upper()
            if key == "PAUSE":
                Logger.log(f"Waiting for {r[1]} seconds", "GREEN")
                sleep(float(r[1]))

            elif key == "#":
                pass

            elif key == "UPGRADE":
                pos = recalc(self.res, target_res, (int(r[1]), int(r[2])))
                self.upgrade_monkey((int(pos[0]), int(pos[1])), r[3])
                Logger.log(f"Upgraded monkey at x:{pos[0]} y:{pos[1]} with path:{r[3]}", "GREEN")

            elif key == "SELL":
                pos = recalc(self.res, target_res, (int(r[1]), int(r[2])))
                self.sell_monkey((int(pos[0], int(pos[1]))))
                Logger.log(f"Sold monkey at x:{pos[0]} y:{pos[1]}")

            elif key == "TARGETING":
                pos = recalc(self.res, target_res, (int(r[1]), int(r[2])))
                self.change_target(pos, int(r[3]))
                Logger.log(f"Changed targeting x:{pos[0]} y:{pos[1]} ") #mode:{"reverse" if int(r[3]) == -1 else "normal"}

            elif key == "SPACE":
                pyautogui.press(PLAY)
                Logger.log(f"Used space", "GREEN")

            elif key == "ABILITY":
                pyautogui.press(r[1])
                Logger.log(f"Used ability {r[1]}", "GREEN")

            else:
                pos = recalc(self.res, target_res, (int(r[1]), int(r[2])))
                self.place_monkey(monkeys[r[0].upper()],(int(pos[0]),int(pos[1])))
                Logger.log(f"Placed {r[0]} at position x:{pos[0]} y:{pos[1]}", "GREEN")