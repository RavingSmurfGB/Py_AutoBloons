import pyautogui, time, termcolor, yaml, pathlib, os, csv
from datetime import datetime
from ahk import AHK

ahk = AHK()

###########################################[TO DO]###########################################

# SETUP
#   have a setup file that installs requirements    

# NEW GAMEPLAN
#   Implement a gameplan_reader
#       Implement terminal questions for:
#           key to stop recording
#           file path for save
#   Disable auto hero select in config.txt
#   XP monkey support will have to be coded individually with different gameplans!!
#       or keep the old playthrough and specify if statements for each xp monkey :P
#   re-create the scaling code in an example and fully document for easy understanding!!
#   Fix the github contents links!
#   Send clicks to the game without it being in front!


#   on each round change call levelcheck()
#   implement verbose instamonkey collection on lvl up

# ISSUES
#   Obyn auto hero slecet NEEDS REWORK AS BLOONS UPDATED THE UI
#   The map will sometimes open the "esc"/ settings menu when upgrading / placing submarine
#   Occasionally the wrong map will be selected
#   Ocasionally the game will be deafeted and not know how to handle
#   Unsure if still occurs, Obyn fails to place

###########################################


###########################################[SETUP]###########################################


# Config file loading...
current_directory = os.getcwd() + "\\"
if "Joe" in current_directory: # Bodge to fix creator's github repo folders...
    current_directory = current_directory + "\\Py_AutoBloons\\"

print(current_directory + "config.txt")


if pathlib.Path(current_directory + "config.txt").is_file():
    print("Cannot find file")
    pass
else:
    with open(current_directory + "config.txt", "w") as file: # Open the file as read
        pass


with open(current_directory + "config.txt") as file: # Open the file as read
    config_file = yaml.load(file, Loader=yaml.FullLoader) # Set the contents to = tmp_current_dictionary

for key, value in config_file.items():
    if key == "Logging":
        if value == None:
            logging = False
        else:
            logging = value
    if key == "XP_Monkey":
        if value == None:
            xp_tower_game = False
            xp_tower = None
        else:
            xp_tower_game = True
            xp_tower = value
    if key == "Gameplan_file": 
        if value == None:
            gameplanFile = "gameplan.csv" # load the defualt plan
        else:
            gameplanFile = value # assign the new value
    if key == "Auto_Hero_Select":
        if value == False:
            autohero_select = False
        else:
            autohero_select = True
    print(key, value) 


if logging == True:
    dt_string = datetime.now().strftime("%H:%M:%S")
    with open("game_log.txt", "a+") as file: #open's the file to allow it to be written to
        file.write("\n" + dt_string + " -- STARTUP \n")# writes to log new startup, includes date/time


def build_gameplan():
    gameplanArray = []
    gameplanFile = "gameplan.csv"
    with open(gameplanFile, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')


        for row in spamreader: 
            gameplanArray.append(row) # We build an array of the list in each row
            # This is used as to not keep the file open in case of a program crash..


width, height = pyautogui.size()
path = current_directory + "Support_Files\\" + str(height) + "_levelup.png"
victory_path = current_directory + "Support_Files\\" + str(height) + "_victory.png"
defeat_path = current_directory + "Support_Files\\" + str(height) + "_defeat.png"
menu_path = current_directory + "Support_Files\\" + str(height) + "_menu.png"
easter_path = current_directory + "Support_Files\\" + str(height) + "_easter.png"
obyn_hero_path = current_directory + "Support_Files\\" + str(height) + "_obyn.png"
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
    "DARK_CASTLE" : [1420, 350], # changed to (x=1941, y=513) in latest patch
    "EASY_MODE" : [838, 550],
    "STANDARD_GAME_MODE" : [847,780],
    "OVERWRITE_SAVE" : [1520, 974],
    "HERO_LOCATION" : [950, 575],
    "SUBMARINE_LOCATION" : [1454, 575],
    "NINJA_LOCATION" : [738, 844],
    "WIZARD_LOCATION" : [736, 645],
    "VICTORY_CONTINUE" : [1283, 1215],
    "VICTORY_HOME" : [957, 1135],
    "EASTER_COLLECTION" : [1279, 911],
    "F_LEFT_INSTA" : [868, 722],
    "F_RIGHT_INSTA" : [1680, 722],
    "LEFT_INSTA" : [1074, 725],
    "RIGHT_INSTA" : [1479, 724],
    "MID_INSTA" : [1276, 727],
    "EASTER_CONTINUE" : [1280, 1330],
    "EASTER_EXIT" : [100, 93],
    "QUIT_HOME" : [1126, 1135],
    "XP_TOWER_1" : [868, 172],
    "XP_TOWER_2" : [1086, 282],
    "HERO_SELECT" : [799, 1272],
    "SELECT_OBYN" : [996, 1296],
    "CONFIRM_HERO" : [855, 893],
    "CHECK_EXIT" : [757, 1088]

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
    ahk.key_press(key) 
    #pyautogui.press(key)
    time.sleep(0.5)

def jtime(seconds):
    #print(seconds)
    time.sleep(seconds)

def Level_Up_Check(seconds):

    #get first time here
    seconds_before = time.time()

    found = pyautogui.locateOnScreen(path, confidence=0.9)

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
        time.sleep(2)  
        press_key("space") # Start the game
        time.sleep(1)
        #press_key("space") # Fast forward the game

    #get second time here
    seconds_after = time.time()
    time_dif = seconds_after - seconds_before # we calculate the difference of time that was used in this function
    
    seconds = seconds - time_dif # we take away the time differance from seconds # how long the script should now wait

    if seconds < 0: # if seconds happened to be a negative (we took more time than seconds was orignaly was to get here)
        seconds = 0

    return seconds
    

def easter_event_check():
    found = pyautogui.locateOnScreen(easter_path, confidence=0.9)
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
        click("F_LEFT_INSTA")
        time.sleep(1)
        click("F_LEFT_INSTA")
        time.sleep(1)
        click("MID_INSTA") # unlock insta
        time.sleep(1)
        click("MID_INSTA") # collect insta
        time.sleep(1)
        click("F_RIGHT_INSTA")
        time.sleep(1)
        click("F_RIGHT_INSTA")
        time.sleep(1)

        time.sleep(1)
        click("EASTER_CONTINUE")


        # awe try to click 3 quick times to get out of the easter mode, but also if easter mode not triggered, to open and close profile quick
        pyautogui.click(tmp_scaling(button_positions["EASTER_EXIT"]))
        time.sleep(1)
        

def victory_check():
    found = pyautogui.locateOnScreen(victory_path, confidence=0.9)
    #jprint(victory_path)
    if found != None:
        jprint("DETECTED -- Victory")

def defeat_check():     
    #jprint(defeat_path)
    found = pyautogui.locateOnScreen(defeat_path, confidence=0.9)
    if found != None:
        jprint("DETECTED -- Defeat")

def menu_check():
    #jprint(menu_path)
    found = pyautogui.locateOnScreen(menu_path, confidence=0.9)
    if found != None:
        jprint("DETECTED -- Menu")
    
    

def place_tower(tower, location, seconds):  # passsssssssssssssssssss time.sleep in to this and before it waits run the level check 
    
    seconds_calc = Level_Up_Check(seconds)

    jprint("placing down " + tower)

    move_mouse(scaling(button_positions[location]))
    press_key(monkeys[tower])
    pyautogui.click()
    time.sleep(0.5)
    if logging == True:
        jprint("Time Delay = " + str(seconds) + " New Time Delay = " + str(seconds_calc))
    jtime(seconds_calc)
    


def upgrade_tower(path, location, seconds): # passsssssssssssssssssss time.sleep in to this and before it waits run the level check 
    seconds_calc = Level_Up_Check(seconds)

    jprint("Upgrading " + location)

    click(location) #Calls click() and passes in the location
    
    press_key(upgrade_path[path]) #Calls press_key() and passes in button
    time.sleep(0.5)
    press_key("esc")
    if logging == True:
        jprint("Time Delay = " + str(seconds) + " New Time Delay = " + str(seconds_calc))
    jtime(seconds_calc)
    
def tmp_scaling(pos_list): # used for easter event, to exit the main menu but without padding (due to 21:9 monitors)
    x = pos_list[0]/2560 
    x = x * width
    y = pos_list[1]/1440
    y = y * height
    return [x, y]


def hero_obyn_check():
    ########################################################################################################################## NEEDS REWORK AS BLOONS UPDATED THE UI
    found = pyautogui.locateOnScreen(obyn_hero_path, confidence=0.9)
    if found == None:
        jprint("STATUS -- Hero not detected, changing hero")
        click("HERO_SELECT")
        click("SELECT_OBYN")
        click("CONFIRM_HERO")
        press_key("esc")




###########################################

###########################################[GAME]###########################################
def Start_Select_Map():
    time.sleep(2)
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
    

def New_Main_Game():

    gameplanArray = []
    gameplanFile = "gameplan.csv"
    with open(gameplanFile, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')


        for row in spamreader: 
            gameplanArray.append(row) # We build an array of the list in each row
            # This is used as to not keep the file open in case of a program crash..

    print(gameplanArray)

    for line in gameplanArray:
        print(line)

            #print("do something here!!"


def Main_Game():
    jprint(" STATUS -- Starting main game")

    defeat_check()
    victory_check()
    menu_check()
    
    time.sleep(2)
    place_tower("HERO", "HERO_LOCATION", 0.5)

    press_key("space") # Start the game
    time.sleep(0.5)
    press_key("space") # Fast forward the game

    time.sleep(20)
    place_tower("SUBMARINE", "SUBMARINE_LOCATION", 8.5)

    upgrade_tower(1, "SUBMARINE_LOCATION", 18)

    upgrade_tower(3, "SUBMARINE_LOCATION", 46)

    upgrade_tower(3, "SUBMARINE_LOCATION", 24)

    upgrade_tower(1, "SUBMARINE_LOCATION", 15)

    place_tower("NINJA", "NINJA_LOCATION", 11.5)

    upgrade_tower(1, "NINJA_LOCATION", 11.5)

    upgrade_tower(1, "NINJA_LOCATION", 4)

    upgrade_tower(3, "NINJA_LOCATION", 12)

    upgrade_tower(1, "NINJA_LOCATION", 23)

    upgrade_tower(3, "SUBMARINE_LOCATION", 39)

    if xp_tower_game == True:
        place_tower(xp_tower, "XP_TOWER_1", 22.5)
        #we place first xp towe in here!!!!
        jtime(Level_Up_Check(22.5))
        # then sleep for 45 sec
        place_tower(xp_tower, "XP_TOWER_2", 20.5)
        #we place second xp tower in now
        # then sleep for 41 sec
        jtime(Level_Up_Check(20.5))
    elif xp_tower_game == False:
        jtime(Level_Up_Check(14.5))
        jtime(Level_Up_Check(14.5))
        jtime(Level_Up_Check(14.5))
        jtime(Level_Up_Check(34.5))

    upgrade_tower(3, "SUBMARINE_LOCATION", 40)
    jtime(Level_Up_Check(1))


def Exit_Game():
    jprint(" STATUS -- Exiting Game, restating loop")

    defeat_check()
    victory_check()
    menu_check()

    
    click("VICTORY_CONTINUE")
    time.sleep(2)
    click("VICTORY_HOME")
    click("CHECK_EXIT") #Code was running into problems restarting
    time.sleep(4)

    easter_event_check()
    time.sleep(2)


###########################################




###########################################[MAIN LOOP]###########################################
jprint("Starting code, move cursor over bloons in the next 5 seconds")
time.sleep(3)
hero_obyn_check()

while True:
    Start_Select_Map()   
    Main_Game()
    Exit_Game()


###########################################
