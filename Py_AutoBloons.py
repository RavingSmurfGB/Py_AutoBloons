import pyautogui, time
from datetime import datetime

###########################################[TO DO]###########################################
# BASICS
#   Store positions in dictionary and referance them via name(key)
#   Have functions that:
#       Can click and accept button_positions
#       Can place monkey (probably made up of other function)
#   Also we will need to find a way to auto accept levels
#       perhaps click in those areas occasionly
#       if fails, check for image in a new thread, if image matches:
#       kill normal thread (have to make it first), accept the stuff,
#       then restart game to main menu and start thread again


# SETUP
#   have a setup file that installs requirements
#   user input resolution, store in file 
#   convert from 2560x1440 to users resolution for button_positions



# OTHER
#   Use hotkey to quit (esc), could use bool, when key press switch state
#       put main function calls in a if statement with that bool, or edit while
#   Different colour text output :)
#   write good readme
#   implement passive xp gain
#       pass in tower to placem, it places it 

###########################################


###########################################[SETUP]###########################################

pyautogui.FAILSAFE = True # When mouse is moved to top left, program will exit

monkeys = {
    "DART" : "Q",
    "BOOMERANG" : "W",
    "BOMB" : "E",
    "TACK" : "R",
    "ICE" : "T",
    "GLUE" : "Y",
    "SNIPER" : "Z",
    "SUBMARINE" : "X",
    "BUCCANEER" : "C",
    "ACE" : "V",
    "HELI" : "B",
    "MORTAR" : "N",
    "DARTLING" : "M",
    "WIZARD" : "A",
    "SUPER" : "S",
    "NINJA" : "D",
    "ALCHEMIST" : "F",
    "DRUID" : "G",
    "BANANA" : "H",
    "ENGINEER" : "L",
    "SPIKE" : "J",
    "VILLAGE" : "K",
    "HERO" : "U"
}



reso_16 = [
    {
        "width": 1280,
        "height": 720        
    },
    {
        "width": 1920,
        "height": 1080
    },
    {
        "width": 2560,
        "height": 1440
    },
    {
        "width": 3840,
        "height": 2160
    }
]

button_positions = { # Creates a dictionary of all positions needed for monkeys (positions mapped to 2160 x 1440 resolution)
    "HOME_MENU_START" : [1123, 1248],
    "EXPERT_SELECTION" : [1778, 1304],
    "RIGHT_ARROW_SELECTION" : [2193, 582],
    "DARK_CASTLE" : [720, 350],
    "EASY_MODE" : [838, 550],
    "STANDARD_GAME_MODE" : [847,780],
    "OVERWRITE_SAVE" : [1520, 974],
    "HERO_LOCATION" : [950, 575],
    "SUBMARINE_LOCATION" : [1454, 575]
}

upgrade_path = {
    1 : ",",
    2 : ".",
    3 : "/"

}

def padding():
# Get's width and height of current resolution
# we iterate through reso_16 for heights, if current resolution height matches one of the entires 
# then it will calulate the difference of the width's between current resolution and 16:9 (reso_16) resolution
# divides by 2 for each side of padding

# Variables Used
#   width -- used to referance current resolution width
#   height -- used to referance current resolution height
#   pad -- used to output how much padding we expect in different resolutions
#   reso_16 -- list that  
    width, height = pyautogui.size()
    pad = 0
    for x in reso_16: 
        if height == x['height']:
            pad = (width - x['width'])/2
    return pad

def scaling(pos_list, do_padding = True):
# This function will dynamically calculate the differance between current resolution and designed for 2560x1440
# it will also add any padding needed to positions to account for 21:9 
    width, height = pyautogui.size()
    x = pos_list[0]/2560 
    y = pos_list[1]/1440
    x = x * width
    y = y * height
    if do_padding == True:
        x + padding() # Add's the pad to to the curent x position variable
    return [x, y]

position = scaling(button_positions["SUBMARINE_LOCATION"])
print(position)

def dynamic_button(button_positions):
    for key in button_positions.keys():
        button_positions[key] = scaling(button_positions[key])
    return button_positions


# Calls dynamic_button and creates a new database taking into account actual resolution
# Then assigns new dictionary returned by dynamic_button() to button_positions
#button_positions = dynamic_button(button_positions) 


def jprint(message):
    dt_string = datetime.now().strftime("%H:%M:%S") #set's the date and time to now
    print(dt_string + " " + message)

def move_mouse(location):
    pyautogui.moveTo(location)
    time.sleep(0.5)

def click(location): #pass in x and y, and it will click for you
    pyautogui.click(scaling(button_positions[location])) # performs the pyautogui click function while passing in the variable from button_positions that matches button
    time.sleep(0.5)

def start_click(location): #pass in x and y, and it will click for you
    pyautogui.click(scaling(button_positions[location], False)) # performs the pyautogui click function while passing in the variable from button_positions that matches button
    time.sleep(0.5)

def press_key(key):
    pyautogui.press(key)
    time.sleep(0.5)
    #pyautogui.keyDown(key)
    #pyautogui.keyUp(key)

def place_tower(tower, location): 
    jprint("placing down " + tower)
    move_mouse(scaling(button_positions[location]))
    press_key(monkeys[tower])
    pyautogui.click()
    time.sleep(0.5)

def upgrade_tower(path, location):

    click(location) #Calls click() and passes in the location
    
    press_key(upgrade_path[path]) #Calls press_key() and passes in button
    time.sleep(0.5)
    press_key("esc")
    

###########################################

###########################################[GAME START]###########################################
def Start_Select_Map():

    jprint("Starting code, move cursor over bloons in the next 5 seconds")
    time.sleep(5)

    jprint("Map Selection in progress")

    start_click("HOME_MENU_START") # Move Mouse and click from Home Menu, Start
    start_click("EXPERT_SELECTION") # Move Mouse to expert and click
    start_click("RIGHT_ARROW_SELECTION") # Move Mouse to arrow and click
    start_click("DARK_CASTLE") # Move Mouse to Dark Castle
    start_click("EASY_MODE") # Move Mouse to select easy mode
    start_click("STANDARD_GAME_MODE") # Move mouse to select Standard mode
    start_click("OVERWRITE_SAVE") # Move mouse to overwrite save if exists
    
###########################################





###########################################[MAIN GAME]###########################################
def Main_Game():
    jprint("Starting main game")
    time.sleep(2)
    place_tower("HERO", "HERO_LOCATION")

    press_key("space") # Start the game
    press_key("space") # Fast forward the game
    time.sleep(8)
    place_tower("SUBMARINE", "SUBMARINE_LOCATION")
    time.sleep(25)
    upgrade_tower(3, "SUBMARINE_LOCATION")
    


###########################################





###########################################[MAIN LOOP]###########################################
# while True:
Start_Select_Map()   
Main_Game()
###########################################