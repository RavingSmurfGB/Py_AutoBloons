# Py_AutoBloons
A Python script that will playthrough the Dark Castle map on Bloons TD 6
- Generayes Monkey Money, Insta-Monkeys, Account Levels and Monkey Experiance!

## Contents
* [How It Works](#how-it-works)
* [Installation](#installation)
* [How To Use](#how-to-use)
* [What Is Needed](#what-is-needed)
* [Compatibility](#compatibility)
* [XP Support](#xp-support)
* [Auto Restart](#auto-restart)
* [Event Support](#event-support)
* [Recording Playthroughs](#recording-playthroughs)


## How It Works
This program will select the map Dark Castle, beat it on easy difficulty, collect any levels, collect any event items, then loop continously.  
It will use the Hero OBYN (Which will be selected auto if not), a submarine and a ninja monkey to beat the gane.  
Please view [What Is Needed](#what-is-needed) to ensure your setup and ready to run the program.  
Please view [XP Support](#xp-support) if you would like this program to automate XP gathring for monkeys.
Using the script auto restart is advised as the script can break occasionaly due to many factors which have not been fully determined yet, see [Auto Restart](#auto-restart)


## Installation
### Manual Install  
 0. Install Python
 1. Extract .zip
 2. Open a CMD window
 3. Enter each command bellow
>       pip install pyautogui
>       pip install pillow
>       pip install termcolor
>       pip install opencv-python
>       pip install pyyaml
>       pip install ahk
>       pip install "ahk[binary]"
>       pip install pynput
>       pip install keyboard
   
## How To Use
 1. Launch Bloons TD 6
 2. Double click Py_AutoBloons.py
 3. Tab back in to Bloons TD 6 within 5 seconds / ensure your cursor is over it   
 \| The Bloons TD 6 Game must be played on your primary monitor.
 \| Auto Start 

## What Is Needed
To run this script ensure that the following upgrades are obtained and the Expert map Dark Castle is unlocked.
Monkey        | Upgrade
------------- | -------------
Submarine     | <ul><li>Longer Range  (Path 1)</li><li>Advanced Intel  (Path 1)</li><li>Twin Guns  (Path 3)</li><li>Airburst Darts  (Path 3)</li><li>Triple Guns  (Path 3)</li><li>Armor Piercing Darts  (Path 3)</li>
Ninja         | <ul><li>Ninja Discipline  (Path 1)</li><li>Sharp Shurikens  (Path 1)</li><li>Double Shot  (Path 1)</li><li>Seeking Shuriken  (Path 3)</li>

## Compatibility
#### Resolutions officialy supported:  
* 1920x1080  
* 2560x1440  
* 3840x2160
#### Other Tips:
\| Resolutions based on the above, but are 21:9 may also work  
\| Resolution refers to your main monitor size, not game resolution  
\| This program was designed to work in Windows but should work in other Operating systems

## XP Support
As mentioned this program can automatically gain XP for towers, this is relatively slow, but over a long AFK time it does add up to a lot.  
By default it is not active, to enable this feature edit the config.txt file follow example there.  
All land monkeys are supported for this feature; Submarine monkeys gain xp by default and Boat monkeys are being worked on currently. 

## Auto Restart
This can be used to close and restart the game occasionly which is extremly helpfull if the script runs in to any issues along its playthrough.
While many bugs have been worked out, due to the complicated nature of automating a game without a API not all will ever be found.
To use this feature you will need to edit the config.txt, instructions for which are provided in config.txt

## Event Support
A new system has been rolled out which should universally detect insta-monkey events, such as the 4th of jully or Easter.
If there are any problems try the To Fix section below and if you still run in to issues open a git-issue.


##DEPRECATED - However may still be usefull if problems arise from insta-monkey events.
With the default behaviour, a insta-monkey event such as the 4th of jully or Easter would break this automated script untill the event is over. 
This is because once the event requirement to give the player an insta-monkey is reached, Bloons will automatically pop up after a game is over and present the "player" with a screen, for which the "player" must click on each insta-monkey.
There is code that will claim these insta-monkeys and return to the game loop, however it works on screen-picture detection, a screenshot is taken at the end of a game which checks if a instamonkey needs to be collected.
However the insta-monkey event changes the user-interface each time, so the picture the code is comparing the screenshot too also needs be changed.
A way to solve this problem automatically is being designed, but there is no expexted ETA for this.
To Fix: 
IF you have problems with insta events - try this: 
* Take a screenshot of the screen that shows up after the game finishes and enters into the insta-monkey event screen
* Save the screenshot and rename to the height of your monitor resolution and append "_easter.png". For example 1080_easter.png
* Navigate to the directory you have saved Py_AutoBloons too, and then enter Support_Files.
* Delete the file you find in that folder, that matches the screenshot you took earlier
* Then copy/paste the new screenshot saved previously into the folder and restart Py_AutoBloons.py

## Recording Playthroughs
With the file "gameplan_recorder" it is possible to build your own play through that "Py_AutoBloons" will use to beat dark castle!!
This is stored by defualt as "gameplan.csv" and can be specified to use in config.txt, however the "gameplan.csv" or whatever you name it will need to be in the same folder as "Py_AutoBloons.py", which may mean you will have to move the .csv file you create.
 
If you are interested in recording your own gameplan to beat a map, timing is very important, try to give yourself a little extra time before buying upgrades to ensure that on another playthrough you will have enough money to buy the same upgrade.
 
Ensure the hero you pick is selected in advance and do not record that section, Also always ensure that you have the correct hero loaded when you go to use the script in the future.

### Instructions
* Start the recorder from the main menu of Bloons TD 6 
* Go to the map and the gamemode you would like to play
* Play through the game, being mindfull to take interactions a little slower than usual, and use hotkeys if you know them!
* End the recorder once you have won and and have pressed the home button from the victory screen.
 

## UPDATES  
11/09/22 - A universal event catch should work to collect insta-monkeys and not break -- Also auto restart has been developed, see config.txt for more information.
