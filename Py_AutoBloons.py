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


# SETUP
#   have a setup file that installs requirements
#   user input resolution, store in file 
#   convert from 2560x1440 to users resolution for button_positions

# RESOLUTION/POSITIONS
#   look into pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)
#       using the above will mean aspect ratio will not matter, only resolution

#   Potentially use pyautogui.screenshot() at start, then find corners of screen,
#       use that to find middle, go to middle and center, then use relatives
#       or use pyautogui.locateCenterOnScreen(image, grayscale=False)

''' # convertion idea, make function to do:
orignal resolution variable, x = 100
orignal resolution = 200

x(100 ) divided by orignal resolution(200) = 0.5

0.5 times by new resolution(400) = 200

new resolution = 400
new resolution variable x = 200
'''
#however doing it bellow method would only work if monitor was in 16:9 ratio, would need more conversion for others
#   we could use a static padding variable to add to x and y to fit the screen
#   could even dynamically figure that out


# OTHER
#   Use hotkey to quit (esc), could use bool, when key press switch state
#       put main function calls in a if statement with that bool, or edit while
#   Different colour text output :)
#   write good readme
#   implement passive xp gain
#       pass in tower to placem, it places it 

###########################################


###########################################[SETUP]###########################################
''' deprocated
resolution = pyautogui.size() # This returns your primary monitor resolution
if resolution == "width=2560, height=1440":
    print("correct resolution continueing ")
else:
    print("Be sure your main monitor is set to 2560 x 1440" )
'''

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

button_positions = {
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
    width, height = pyautogui.size()
    pad = 0
    for x in reso_16:
        if height == x['height']:
            pad = (width - x['width'])/2
    return pad

def scaling(pos_list):
    width, height = pyautogui.size()
    if width == 1440:
        return pos_list
    x = pos_list[0]/2560 
    y = pos_list[1]/1440
    x = x * width
    y = y * height
    x + padding()
    return [x, y]

def dynamic_button(button_positions):
    for key in button_positions.keys():
        button_positions[key] = scaling(button_positions[key])
    return button_positions

button_positions = dynamic_button(button_positions)

def jprint(message):
    dt_string = datetime.now().strftime("%H:%M:%S") #set's the date and time to now
    print(dt_string + " " + message)

def sleep(): # Used for spacing in between commands
    time.sleep(0.5)

def move_mouse(location):
    pyautogui.moveTo(location)
    sleep()



def click(location): #pass in x and y, and it will click for you
    pyautogui.click(button_positions[location]) # performs the pyautogui click function while passing in the variable from button_positions that matches button
    sleep()

def re_allign():
    print()

def press_key(key):
    pyautogui.press(key)
    sleep()
    #pyautogui.keyDown(key)
    #pyautogui.keyUp(key)

def place_tower(tower, location): 
    jprint("placing down " + tower)
    
    move_mouse(button_positions[location])
    press_key(monkeys[tower])
    pyautogui.click()
    sleep()
    #re_allign()


def upgrade_tower(path, location):

    click(location) #Calls click() and passes in the location
    
    press_key(upgrade_path[path]) #Calls press_key() and passes in button
    sleep()
    press_key("esc")
    

def level_check():
    print()

###########################################[

###########################################[GAME START]###########################################
def Start_Select_Map():

    jprint("Starting code, move cursor over bloons in the next 5 seconds")
    time.sleep(5)

    jprint("Map Selection in progress")

    click("HOME_MENU_START") # Move Mouse and click from Home Menu, Start
    click("EXPERT_SELECTION") # Move Mouse to expert and click
    click("RIGHT_ARROW_SELECTION") # Move Mouse to arrow and click
    click("DARK_CASTLE") # Move Mouse to Dark Castle
    click("EASY_MODE") # Move Mouse to select easy mode
    click("STANDARD_GAME_MODE") # Move mouse to select Standard mode
    click("OVERWRITE_SAVE") # Move mouse to overwrite save if exists
    
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