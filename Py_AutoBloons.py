import pyautogui, time

###########################################[TO DO]###########################################
# BASICS
#   Store positions in dictionary and referance them via name(key)
#   Have functions that:
#       Can click and accept button_positions
#       Can place monkey (probably made up of other function)

# SETUP
#   have a setup file that installs requirements
#   user input resolution, store in file 
#   convert from 2560x1440 to users resolution for button_positions

#   Write 


###########################################


###########################################[SETUP]###########################################

resolution = pyautogui.size() # This returns your virtual resolution for your entire desktop
if resolution == "width=2560, height=1440":
    print("correct resolution continueing ")
else:
    print("Be sure your main monitor is set to 2560 x 1440" )





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

button_positions = {
    "HOME_MENU_START" : [1123, 1248],
    "EXPERT_SELECTION" : [1778, 1304],
    "RIGHT_ARROW_SELECTION" : [2193, 582],
    "DARK_CASTLE" : [720, 350],
    "EASY_MODE" : [838, 550],
    "STANDARD_GAME_MODE" : [847,780],
    "OVERWRITE_SAVE" : [1520, 974]

}

#print(button_positions["HOME_MENU_START"]) # Gets home menu starting postion from dictionary


upgrade_path = {
    "PATH_1" : ",",
    "PATH_2" : ".",
    "PATH_3" : "-"

}
 

def sleep(): # Used for spacing in between commands
    time.sleep(1)


def click(button): #pass in x and y, and it will click for you
    #button_positions[button]
    pyautogui.click(button_positions[button])
    sleep()


###########################################[

###########################################[GAME START]###########################################
def Start_Select_Map():

    print("Starting code, move cursor over bloons in the next 5 seconds")
    time.sleep(5)

    print("Map Selection in progress")

    click("HOME_MENU_START") # Move Mouse and click from Home Menu, Start
    click("EXPERT_SELECTION") # Move Mouse to expert and click
    click("RIGHT_ARROW_SELECTION") # Move Mouse to arrow and click
    click("DARK_CASTLE") # Move Mouse to Dark Castle
    click("EASY_MODE") # Move Mouse to select easy mode
    click("STANDARD_GAME_MODE") # Move mouse to select Standard mode
    click("OVERWRITE_SAVE") # Move mouse to overwrite save if exists


Start_Select_Map()   
###########################################[


###########################################[MAIN GAME]###########################################



###########################################