
import pyautogui, os

current_directory = os.getcwd() + "\\"

current_directory = current_directory + "\\Py_AutoBloons\\"


easter_path = current_directory + "Support_Files\\" + "1440_event.fw.png"

found = pyautogui.locateOnScreen(easter_path, confidence=0.9)
if found != None:
    print(found)