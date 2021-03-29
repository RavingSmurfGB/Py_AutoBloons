import pyautogui, termcolor


width, height = pyautogui.size()
path = "Support_Files\\" + str(height) + "_levelup.png"
path = "Support_Files\\1080_levelup.png"
print(path)

## this in thread:
def Level_Up_Check():

    found = pyautogui.locateOnScreen(path)
    if found != None:
        print("Found image")
    elif found == None:
        print("Could not find image")

Level_Up_Check()