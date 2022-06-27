from ahk import AHK
import time

time.sleep(5)

ahk = AHK()

win = ahk.find_window(title=b'Untitled - Notepad') # Find the opened window

for window in ahk.windows():
    #print(window.title)
    if "Bloons" in str(window.title):
        window = window.title
        print("foung bllons!")

        win = ahk.find_window(title=window) # Find the opened window

        win.send("q")
        win.minimize()

