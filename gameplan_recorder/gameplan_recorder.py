from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from datetime import datetime
from pynput import mouse
import csv, os, time, pyautogui


'''
We base this recording script from the main srcipt able to mouse up and mouse down sepreatly!

pyautogui.mouseDown(button='right')  # press the right button down
pyautogui.mouseUp(button='right', x=100, y=200)  # move the mouse to 100, 200, then release the right button up.
'''

#   RECORD MILLISCEONDS ASWELL!!!!

#Main variables
gameplanArray = [] # Used as the full gamplan, containing time, press and location



os.system('cls||clear')
print("Recorder Starting...")

end_key = input("Enter the key you wish to use to end recording : ") or "`" # Defines the key used to end the script
print("Use the ", end_key, " key to stop recording")
print("\n")
time.sleep(0.5)




file_save = input("Enter the name of the recording : ") or "gameplan.csv" # Where should the data recorded be saved
if ".csv" not in file_save: # Check for the csv extension
    file_save = file_save + ".csv" # if not in add it..

file_path = os.getcwd()
if "DESKTOP-7HL22EH" in os.environ['COMPUTERNAME']: # Bodge to fix creator's github repo folders...

    file_path = file_path + "\\Py_AutoBloons"
file_path = file_path + "\\" + file_save


print("The file will be saved to ", file_path )
print("\n")
time.sleep(0.5)




def on_press(key):
    # This function monitors for key presses, if it matches the end_key, it will write the gameplanArray to the file and close the program
    #
    # Variables used:
    #   gameplanArray - we add the eventclickArray to this and save to file
    #   file_save - The location where we save the gameplan to
    #   end_key - is the key that is pressed to trigger the if statement

    if key.char == end_key:
        print("The recorder will now end, saving to file...")
        

        with open(file_path, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for line in gameplanArray:
                spamwriter.writerow(line)
        print("The file has been saved to " , file_path)
        os._exit(0) # We exit the script
    


    


def on_click(x, y, button, pressed):
    # This function is used to gather data about the click and release events, then feed back in to the gameplanArray
    #
    # Variables used:
    #   pressed - used in determining updown
    #   updown - detemine from pressed, to see if the mouse was clicked or released
    #   location - this contains the location of where was clicked5
    #   time - this is set to the current time of when the mouse was clicked
    #   eventclickArray - this is used to join, updown, location and  time
    #   gameplanArray - we add the eventclickArray to this 
    #   actual_time - Used to calculate time_diff and saved to gameplanArray
    #   resolution - Uused for scaling logic in Py_autobloons, contains height & width


    if button == mouse.Button.left:  # We check if the left button is pressed
  
        if pressed == True: #if the button was pressed or released we assign it to the variable updown
            updown = "Pressed"
        elif pressed == False:
            updown = "Released"

        location = (x, y) # Assign location the X and Y of the mouse cursor
        time = datetime.now().strftime("%H:%M:%S.%f") # Returns the current time as a string
        actual_time = time # We store the actual_time as a seperate variable


        array_length = len(gameplanArray) # This line is used to see how big the array is
        if array_length != 0: # If the gameplanArray is empty then do nothing, 
            array_length -= 1 # We have to minus one, as arrays are indexed from 0 but length start from 1

            timeDT = datetime.strptime(time,"%H:%M:%S.%f") # We convert the current time to a date time object

            row_before_timeDT = datetime.strptime(gameplanArray[array_length][3],"%H:%M:%S.%f") # We get the last actual_time and convert it to a date time object

            time_diff =  timeDT - row_before_timeDT # We take away current time from previous time...

            time_diff = str(time_diff.total_seconds())# We convert time_diff to a string and only capture the total amount of seconds
            
           
        
        elif array_length == 0:# On the first iteration, it is not possible to see the time before,
            time_diff = "0" # we simply set the time_diff to 0

        #time_diff = sum(x * int(t) for x, t in zip([3600, 60, 1], time_diff.split(":"))) # We convert the time string in to a integer before saving


        width, height = pyautogui.size()
        resolution = (width, height)# we capture the resolution and add it to the eventclickArray, this is used for scaling logic in Py_autobloons
        eventclickArray = [time_diff, updown, location, actual_time, resolution] # Assign all the variables to a list
        print("Mouse Event captured at - " , location)
        gameplanArray.append(eventclickArray)# Add eventclickArray to gameplanArray







# Setup the listener threads
keyboard_listener = KeyboardListener(on_press=on_press)
mouse_listener = MouseListener(on_click=on_click)

# Start the threads and join them so the script doesn't end earlyd
keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()









