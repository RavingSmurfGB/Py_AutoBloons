import pyautogui, termcolor


width, height = pyautogui.size()

## this in thread:
path = "Support_Files\\" + str(height) + "_levelup.png"
found = pyautogui.locateOnScreen(path)
if found != None:
    # here run code to handle level ups, will have to also implement insta collect
    print(found)




print(termcolor.colored("hi", "green")) 