import pyautogui, time, termcolor
from datetime import datetime

###########################################[TO DO]###########################################
# BASICS
#   Store positions in dictionary and referance them via name(key)                      Done
#   Have functions that:
#       Can click and accept button_positions                                           Done    
#       Can place monkey (probably made up of other function)                           Done
#   Have code start game                                                                Done
#   Have code beat game                                                                 Done
#   Have code exit to main menu                                                         
#   Loop all above in function
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



#ISSUES
#   believe that math doesnt work for converting to other aspect ratios
#       this is because we are trying to convert the resolution to 3440x1440 then add padding
#       what we need to do is not touch the resolution if the 1440 matches, then simply add padding
#       if resolution is not 16:9 leave x (horizontal) axis alone
#       



#   21:9 ASPECT ration convertion doesnt work
#   pixels are off horizontaly
#   perhaps just get user to add in manually to button_positions
#       however depending on how we handle levels this could be a problem


''' code positions
HOME_MENU_START
 Me wihout padding [1509.03125, 1248.0]
I have been padding -- 440.0
 Me with padding -- [1509.03125, 1248.0]
EXPERT_SELECTION
 Me wihout padding [2389.1875, 1304.0]
I have been padding -- 440.0
 Me with padding -- [2389.1875, 1304.0]
 '''
''' # actual posiution on sean scren
home_menu start 1552, 1248
expert_selection 2227 1308
'''
###########################################


###########################################[SETUP]###########################################

logging = True

if logging == True:
    dt_string = datetime.now().strftime("%H:%M:%S")
    with open("game_log.txt", "a+") as file: #open's the file to allow it to be written to
        file.write("\n" + dt_string + " -- STARTUP \n")# writes to log new startup, includes date/time

width, height = pyautogui.size()
path = "Support_Files\\" + str(height) + "_levelup.png"
victory_path = "Support_Files\\" + str(height) + "_victory.png"
defeat_path = "Support_Files\\" + str(height) + "_defeat.png"
menu_path = "Support_Files\\" + str(height) + "_menu.png"
easter_path = "Support_Files\\" + str(height) + "_easter.png"
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
    "SUBMARINE_LOCATION" : [1454, 575],
    "NINJA_LOCATION" : [738, 844],
    "WIZARD_LOCATION" : [736, 645],
    "VICTORY_CONTINUE" : [1283, 1215],
    "VICTORY_HOME" : [1057, 1135],
    "EASTER_COLLECTION" : [1279, 911],
    "LEFT_INSTA" : [1074, 725],
    "RIGHT_INSTA" : [1479, 724],
    "MID_INSTA" : [1279, 724],
    "EASTER_CONTINUE" : [1280, 1330],
    "EASTER_EXIT" : [100, 93],
    "QUIT_HOME" : [1126, 1135]

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
    #print("I have been padding -- " + str(pad))

    return pad

def scaling(pos_list):
# This function will dynamically calculate the differance between current resolution and designed for 2560x1440
# it will also add any padding needed to positions to account for 21:9 

# do_padding -- this is used during start 
    reso_21 = False
    width, height = pyautogui.size()
    for x in reso_16: 
        if height == x['height']:
            if width != x['width']:
                reso_21 = True
                x = pos_list[0]
                break
    if reso_21 != True:
        x = pos_list[0]/2560 
        x = x * width
    y = pos_list[1]/1440
    y = y * height
    #print(" Me wihout padding " + str([x]))
    x = x + padding() # Add's the pad to to the curent x position variable
    #print(" Me with padding -- " + str([x]))
    return [x, y]

def jprint(message):

    # print(termcolor.colored("hi", "green")) 
    dt_string = datetime.now().strftime("%H:%M:%S") #set's the date and time to now
    print(dt_string + " " + termcolor.colored(message, "green"))
    if logging == True:
        dt_string = datetime.now().strftime("%H:%M:%S")
        with open("game_log.txt", "a+") as file: #open's the file to allow it to be written to
            file.write(dt_string + " -- " + message + "\n")# writes to log new startup, includes date/time

def move_mouse(location):
    pyautogui.moveTo(location)
    time.sleep(0.5)

def click(location): #pass in x and y, and it will click for you
    #print(location)
    pyautogui.click(scaling(button_positions[location])) # performs the pyautogui click function while passing in the variable from button_positions that matches button
    time.sleep(0.5)


def press_key(key):
    pyautogui.press(key)
    time.sleep(0.5)


def Level_Up_Check():

    found = pyautogui.locateOnScreen(path)
    if found != None:
        jprint("DETECTED -- Level UP")

        click("LEFT_INSTA") # Accept lvl
        time.sleep(1)
        click("LEFT_INSTA") # Accept knoledge
        time.sleep(1)

        click("LEFT_INSTA") # unlock insta
        time.sleep(1)
        click("LEFT_INSTA") # collect insta
        time.sleep(1)

        click("MID_INSTA") # unlock insta
        time.sleep(1)
        click("MID_INSTA") # collect insta
        time.sleep(1)

        click("RIGHT_INSTA") # unlock r insta
        time.sleep(1)
        click("RIGHT_INSTA") # collect r insta
        time.sleep(51)  
        press_key("space") # Start the game
        press_key("space") # Fast forward the game

def easter_event_check():
    found = pyautogui.locateOnScreen(easter_path)
    if found != None:
        jprint("DETECTED -- Easter")
        click("EASTER_COLLECTION") #DUE TO EASTER EVENT:
        time.sleep(1)
        click("LEFT_INSTA") # unlock insta
        time.sleep(1)
        click("LEFT_INSTA") # collect insta
        time.sleep(1)
        click("RIGHT_INSTA") # unlock r insta
        time.sleep(1)
        click("RIGHT_INSTA") # collect r insta
        time.sleep(1)
        click("EASTER_CONTINUE")
        time.sleep(1)

        # awe try to click 3 quick times to get out of the easter mode, but also if easter mode not triggered, to open and close profile quick
        pyautogui.click(tmp_scaling(button_positions["EASTER_EXIT"]))
        time.sleep(1)
        



def victory_check():
    found = pyautogui.locateOnScreen(victory_path)
    jprint(victory_path)
    if found != None:
        jprint("DETECTED -- Victory")

def defeat_check():     
    jprint(defeat_path)
    found = pyautogui.locateOnScreen(defeat_path)
    if found != None:
        jprint("DETECTED -- Defeat")

def menu_check():
    jprint(menu_path)
    found = pyautogui.locateOnScreen(menu_path)
    if found != None:
        jprint("DETECTED -- Menu")
    
    

def place_tower(tower, location):  # passsssssssssssssssssss time.sleep in to this and before it waits run the level check 
    Level_Up_Check()
    jprint("placing down " + tower)
    move_mouse(scaling(button_positions[location]))
    press_key(monkeys[tower])
    pyautogui.click()
    time.sleep(0.5)


def upgrade_tower(path, location): # passsssssssssssssssssss time.sleep in to this and before it waits run the level check 
    Level_Up_Check()
    jprint("Upgrading " + location)

    click(location) #Calls click() and passes in the location
    
    press_key(upgrade_path[path]) #Calls press_key() and passes in button
    time.sleep(0.5)
    press_key("esc")
    
def tmp_scaling(pos_list): # used for easter event, to exit the main menu but without padding (due to 21:9 monitors)
    x = pos_list[0]/2560 
    x = x * width
    y = pos_list[1]/1440
    y = y * height
    return [x, y]

###########################################

###########################################[GAME]###########################################
def Start_Select_Map():

    jprint("Starting code, move cursor over bloons in the next 5 seconds")
    time.sleep(5)



    jprint("STATUS -- Map Selection in progress")

    defeat_check()
    victory_check()
    menu_check()

    click("HOME_MENU_START") # Move Mouse and click from Home Menu, Start
    click("EXPERT_SELECTION") # Move Mouse to expert and click
    click("RIGHT_ARROW_SELECTION") # Move Mouse to arrow and click
    click("DARK_CASTLE") # Move Mouse to Dark Castle
    click("EASY_MODE") # Move Mouse to select easy mode
    click("STANDARD_GAME_MODE") # Move mouse to select Standard mode
    click("OVERWRITE_SAVE") # Move mouse to overwrite save if exists
    

def Main_Game():
    jprint(" STATUS -- Starting main game")


    defeat_check()
    victory_check()
    menu_check()

    
    time.sleep(2)
    place_tower("HERO", "HERO_LOCATION")

    press_key("space") # Start the game
    press_key("space") # Fast forward the game
    time.sleep(8)
    place_tower("SUBMARINE", "SUBMARINE_LOCATION")
    time.sleep(8.5)
    upgrade_tower(1, "SUBMARINE_LOCATION")
    time.sleep(18)
    upgrade_tower(3, "SUBMARINE_LOCATION")
    time.sleep(46)
    upgrade_tower(3, "SUBMARINE_LOCATION")
    time.sleep(24)
    upgrade_tower(1, "SUBMARINE_LOCATION")
    time.sleep(15)
    place_tower("NINJA", "NINJA_LOCATION")
    time.sleep(11.5)
    upgrade_tower(1, "NINJA_LOCATION")
    time.sleep(11.5),
    upgrade_tower(1, "NINJA_LOCATION")
    time.sleep(4)
    upgrade_tower(3, "NINJA_LOCATION")
    time.sleep(12)
    upgrade_tower(1, "NINJA_LOCATION")
    time.sleep(8)
    place_tower("WIZARD", "WIZARD_LOCATION")
    time.sleep(5)
    upgrade_tower(2, "WIZARD_LOCATION")
    time.sleep(9)
    upgrade_tower(2, "WIZARD_LOCATION")
    time.sleep(51)
    upgrade_tower(2, "WIZARD_LOCATION")
    time.sleep(43)
    upgrade_tower(1, "NINJA_LOCATION")
    time.sleep(5)
    upgrade_tower(3, "SUBMARINE_LOCATION")
    time.sleep(30)
    upgrade_tower(3, "SUBMARINE_LOCATION")
    time.sleep(25)

def Exit_Game():



    jprint(" STATUS -- Exiting Game, restating loop")

    defeat_check()
    victory_check()
    menu_check()

    
    click("VICTORY_CONTINUE")
    time.sleep(2)
    click("VICTORY_HOME")
    time.sleep(4)

    easter_event_check()
    time.sleep(2)




    


###########################################





###########################################[MAIN LOOP]###########################################

while True:
    Start_Select_Map()   
    Main_Game()


###########################################
