from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from datetime import datetime
from pynput import mouse
import csv, os

'''
We base this recording script from the main srcipt able to mouse up and mouse down sepreatly!

pyautogui.mouseDown(button='right')  # press the right button down
pyautogui.mouseUp(button='right', x=100, y=200)  # move the mouse to 100, 200, then release the right button up.
'''

#Main variables
gameplanArray = [] # Used as the full gamplan, containing time, press and location
end_key = "`" # Defines the key used to end the script
file_save = "gameplan.csv" # Where should the data recorded be saved


def on_press(key):
    # This function monitors for key presses, if it matches the end_key, it will write the gameplan to the file and close the program
    #
    # Variables used:
    #   gameplan - we add the eventclickArray to this and save to file
    #   file_save - The location where we save the gameplan to
    #   end_key - is the key that is pressed to trigger the if statement
    global gameplan
    if key.char == end_key:
        print("the a key was pressed!")


        with open(file_save, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for line in gameplanArray:
                spamwriter.writerow(line)

        os._exit(0)
    


    


def on_click(x, y, button, pressed):
    # This function is used to gather data about the click and release events, then feed back in to the gameplanArray
    #
    # Variables used:
    #   pressed - used in determining updown
    #   updown - detemine from pressed, to see if the mouse was clicked or released
    #   location - this contains the location of where was clicked5
    #   time - this is set to the current time of when the mouse was clicked
    #   eventclickArray - this is used to join, updown, location and  time
    #   gameplan - we add the eventclickArray to this 
    global gameplan

    if button == mouse.Button.left:  # We check if the left button is pressed

        if pressed == True: #if the button was pressed or released we assign it to the variable updown
            updown = "Pressed"
        elif pressed == False:
            updown = "Released"

        location = (x, y) # location simply states where the mouse click event was
        time = datetime.now().strftime("%H:%M:%S") # we get the time of the events

        eventclickArray = [time, updown, location,]


        gameplanArray.append(eventclickArray)
        print(gameplanArray)



# Setup the listener threads
keyboard_listener = KeyboardListener(on_press=on_press)
mouse_listener = MouseListener(on_click=on_click)

# Start the threads and join them so the script doesn't end earlyd
keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()









