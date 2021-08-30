import pyautogui, time, termcolor, yaml, pathlib, os, csv
from datetime import datetime

###########################################[TO DO]###########################################

# SETUP
#   have a setup file that installs requirements    

# NEW GAMEPLAN
#   Implement a gameplan_reader
#       Implement terminal questions for:
#           key to stop recording
#           file path for save
#       move gameplan save location to under gameplan recorder
#
#   ISSUE : Current gameplan_recording will only work to play back on same aspect ratios, we arent able to remove padding e.g. 16.9 - 16.9 = good, 21.9 - 16.9 = bad
#
#   Disable auto hero select in config.txt
#   XP monkey support will have to be coded individually with different gameplans!!
#       or keep the old playthrough and specify if statements for each xp monkey :P
#   re-create the scaling code in an example and fully document for easy understanding!!
#   Fix the github contents links!
#   Implement key to stop the script
#   Send clicks to the game without it being in front!


#   on each round change call levelcheck()
#   implement verbose instamonkey collection on lvl up


###########################################


###########################################[SETUP]###########################################


os.system('cls||clear')
# Config file loading...
current_directory = os.getcwd()
if "DESKTOP-7HL22EH" in os.environ['COMPUTERNAME']: # Bodge to fix creator's github repo folders...
    current_directory = current_directory + "\\Py_AutoBloons\\"

print("Loading config file - " , current_directory + "config.txt")


if pathlib.Path(current_directory + "config.txt").is_file():
    
    pass
else:
    print("Cannot find file")
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
            file_path = os.getcwd()
            if "DESKTOP-7HL22EH" in os.environ['COMPUTERNAME']: # Bodge to fix creator's github repo folders..
                gameplanFile = file_path + "\\Py_AutoBloons" "\\" + gameplanFile

        else:
            gameplanFile = value # assign the new value
        print(file_path)
    if key == "Auto_Hero_Select":
        if value == False:
            auto_hero_select = False
        else:
            auto_hero_select = True
 


if logging == True:
    dt_string = datetime.now().strftime("%H:%M:%S")
    with open("game_log.txt", "a+") as file: #open's the file to allow it to be written to
        file.write("\n" + dt_string + " -- STARTUP \n")# writes to log new startup, includes date/time


gameplanArray = [] # We create a global variable to build the gameplan
def build_gameplan():
    
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
    "VICTORY_HOME" : [1057, 1135],
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
    "CONFIRM_HERO" : [855, 893]

}


upgrade_path = {
    1 : ",",
    2 : ".",
    3 : "/"

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

def scaling(location, orignal_resolution):
# This function will dynamically calculate the differance between current resolution and the script which is designed for 2560x1440
# However with the implementation of gameplan_recorder this will not work for anything other than my resolution
# it will also add any padding needed to positions to account for 21:9 

# do_padding -- this is used during start 
    reso_21 = False
    width, height = pyautogui.size()
    for x in reso_16: 
        if height == x['height']:
            if width != x['width']:
                reso_21 = True
                x = location[0]
                break
    if reso_21 != True: # If the current resolution is not 16:9
        x = location[0]/orignal_resolution[0] # We divide the width(x) of where the mouse should click by the orignal resolution
        x = x * width # we then multiply the width(x) by the width of the current resolution
    y = location[1]/orignal_resolution[1] # We divide the height(y) of where the mouse should click by the orignal resolution
    y = y * height # we then multiply the height(y) by the height of the current resolution

 
    x = x + padding() # Add's the pad to to the curent x position variable, used for 21:9 resolutions
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
    if auto_hero_select == True:
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
    






def click_updown(locationxy, updown, orignal_resolution):
    print(locationxy)
    scaling_location = scaling(locationxy, orignal_resolution)
    print(scaling_location)
    if updown == "Pressed":
        
        #pyautogui.moveTo(scaling_location[0], scaling_location[1])
        pyautogui.moveTo(scaling_location[0], scaling_location[1])
        time.sleep(0.2)
        pyautogui.mouseDown(button='left')

            
    elif updown == "Released":
        #pyautogui.dragTo(scaling_location[0], scaling_location[1], 0.3,button='left')
        pyautogui.moveTo(scaling_location[0], scaling_location[1])
        time.sleep(0.2)
        pyautogui.mouseUp(button='left')


    






def New_Main_Game():
    time.sleep(3)
    for line in gameplanArray:
        print(line)
        time_delay = float(line[0])# We convert the time delay to a float to enable milliseonds
        print(time_delay)
        print(type(time_delay))
        updown = line[1]
        #locationxy = line[2]
        locationxy = eval(line[2]) # We get the location of 
        orignal_resolution = eval(line[4]) # We get the location of 
        click_updown(locationxy, updown, orignal_resolution )
        if time_delay == 0:
            time_delay = 0.5
        time.sleep(time_delay)
          

# CURRENT ISSUE - drag towers seems to not work # seems to be that the mouse up command is not triggering the tower to place # worked around by seperating the move command and click command
#       timing also seems to  still be an issue















def Main_Game():
    jprint(" STATUS -- Starting main game")

    defeat_check()
    victory_check()
    menu_check()
    
    time.sleep(2)
    place_tower("HERO", "HERO_LOCATION", 0.5)

    press_key("space") # Start the game
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
    time.sleep(4)

    easter_event_check()
    time.sleep(2)


def round_based_loop():
    timings = 0

    #SETUP
    jprint(" STATUS -- Starting main game")

    defeat_check()
    victory_check()
    menu_check()
    
    time.sleep(2)
    place_tower("HERO", "HERO_LOCATION", 0.5)

    press_key("space") # Start the game
    press_key("space") # Fast forward the game
    time.sleep(1) # pushes back all the 

    #ROUND 1: 9 seconds, 119 cash , hero placed 550
    jtime(Level_Up_Check(9))

    #ROUND 2: 9.5 seconds, 252 cash, 
    jtime(Level_Up_Check(9.5))

    #ROUND 3: 10.2 seconds, 111 cash, sub placed 275
    place_tower("SUBMARINE", "SUBMARINE_LOCATION", timings)
    jtime(Level_Up_Check(10.2))
    
    #ROUND 4: 9 seconsd, 221 cash, 
    jtime(Level_Up_Check(9))

    #ROUND 5: 20 seconds, 450 cash, sub upgraded 110
    upgrade_tower(1, "SUBMARINE_LOCATION", timings)
    jtime(Level_Up_Check(20))

    #ROUND 6: 10 seconds, 233 cash, sub upgraded 380
    upgrade_tower(3, "SUBMARINE_LOCATION", timings)
    jtime(Level_Up_Check(10))

    #ROUND 7: 14 seconds, 415 cash, 
    jtime(Level_Up_Check(14))

    #ROUND 8: 14.2 seconds, 615 cash,
    jtime(Level_Up_Check(14.2))

    #ROUND 9: 10.3 seconds,  814 cash 
    jtime(Level_Up_Check(10.3))

    #ROUND 10: 25 seconds, 278 cash, sub upgraded 850
    upgrade_tower(3, "SUBMARINE_LOCATION", timings)
    jtime(Level_Up_Check(25))

    #ROUND 11: 11.2 seconds, 42 cash, sub upgraded 425
    upgrade_tower(1, "SUBMARINE_LOCATION", timings)
    jtime(Level_Up_Check(11.2))

    #ROUND 12: 6.3 seconds, 234 cash,
    jtime(Level_Up_Check(6.3))

    #ROUND 13: 13.2 seconds, 516 cash, ninja placed 425  
    place_tower("NINJA", "NINJA_LOCATION", timings)
    jtime(Level_Up_Check(13.2))

    #ROUND 14: 14.1 seconds, 350 cash, ninja upgraded 255, ninja upgraded 295
    upgrade_tower(1, "NINJA_LOCATION", timings)
    upgrade_tower(1, "NINJA_LOCATION", timings)
    jtime(Level_Up_Check(14.1))

    #ROUND 15: 14.1 seconds, 361 cash, ninja upgraded 210, ninja upgraded 720
    upgrade_tower(3, "NINJA_LOCATION", timings)
    upgrade_tower(1, "NINJA_LOCATION", timings)
    jtime(Level_Up_Check(14.1))

    #ROUND 16: 8.1 seconds, 334 cash
    jtime(Level_Up_Check(8.1))

    #ROUND 17: 3 seconds, 289 cash
    jtime(Level_Up_Check(17.3))

    #ROUND 18: 14.1 seconds, 647 cash, 
    jtime(Level_Up_Check(14.5))

    #ROUND 19: 7.2 seconds, 187 cash
    jtime(Level_Up_Check(7.2))

    #ROUND 20: 3.25 seconds, 373 cash
    jtime(Level_Up_Check(3.3))

    #ROUND 21: 9.27 seconds 724 cash, 
    jtime(Level_Up_Check(9.27))

    #ROUND 22: 5.1 seconds, 1022 cash,
    jtime(Level_Up_Check(5.1))

    #ROUND 23: 4.1 seconds, 364 cash, sub upgraded 975
    upgrade_tower(3, "SUBMARINE_LOCATION", timings)
    jtime(Level_Up_Check(4.1))

    #ROUND 24: 7 seconds, 559 cash
    jtime(Level_Up_Check(7))

    #ROUND 25: 6.3 seconds, 866 cash
    jtime(Level_Up_Check(6.3))

    #ROUND 26: 7.1 seconds, 1199 cash
    jtime(Level_Up_Check(7.1))

    #ROUND 27: 13.2 seconds, 1861 cash
    jtime(Level_Up_Check(13.2))

    #ROUND 28: 3.15 seconds, 2127 cash
    jtime(Level_Up_Check(3.15))

    #ROUND 29: 6.18 seconds, 2516 cash
    jtime(Level_Up_Check(6.18))

    #ROUND 30: 7 seconds, 2854 cash
    jtime(Level_Up_Check(7))

    #ROUND 31: 7 seconds, 3390 cash
    jtime(Level_Up_Check(7))

    #ROUND 32: 11.18 seconds, 4017 cash
    jtime(Level_Up_Check(11.18))

    #ROUND 33: 10.18 seconds, 4222 cash
    jtime(Level_Up_Check(10.18))

    #ROUND 34: 14.03 seconds, 5134 cash
    jtime(Level_Up_Check(14.03))

    #ROUND 35: 14.15 seconds, 6337 cash
    jtime(Level_Up_Check(14.15))

    #ROUND 36: 8.09 seconds. 7180 cash
    upgrade_tower(3, "SUBMARINE_LOCATION", timings)
    jtime(Level_Up_Check(14.5))

    #ROUND 37: 17.17 seconds, 8519 cash
    jtime(Level_Up_Check(17.17))

    #ROUND 38: 13.21 seconds, 9762 cash
    jtime(Level_Up_Check(13.21))

    #ROUND 39: 21.08 seconds, 9478 cash, sub upgraded 2550
    jtime(Level_Up_Check(21.08))


###########################################





###########################################[MAIN LOOP]###########################################
build_gameplan()
New_Main_Game()


'''
jprint("Starting code, move cursor over bloons in the next 5 seconds")
time.sleep(3)
hero_obyn_check()

while True:
    Start_Select_Map()   
    # round_based_loop()
    Main_Game()

    Exit_Game()
'''


###########################################