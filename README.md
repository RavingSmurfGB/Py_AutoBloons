# Py_AutoBloons
 *This Script is undergoing a re-write, to make creating your own level designs easier and optimising the way to record a gameplan.
Stay tuned for further updates!*.

A Python script that will beat Bloons TD 6 on Dark Castle.  
Gives Monkey Money, Insta-Monkeys, Account Leve;s, Monkey Experiance!

## Contents
* [How It Works](#How_It_Works)
* [Installation](#Installation)
* [How To Use](#How_To_Use)
* [What Is Needed](#What_Is_Needed)
* [Compatibility](#Compatibility)
* [XP Support](#XP_Support)
* [Recording Playthroughs](#Recording_Playthroughs)


## How It Works
This program will select the map Dark Castle, beat it on easy difficulty, collect any levels, collect any event items, then loop continously.  
It will use the Hero OBYN (Which will be selected auto if not), a submarine and a ninja monkey to beat the gane.  
Please view [What Is Needed](#What_Is_Needed)<a name="What_Is_Needed"></a> to ensure your setup and ready to run the program.  
Please view [XP Support](#XP_Support)<a name="XP_Support"></a> if you would like this program to automate XP gathring for monkeys.


## Installation
### Automatic Install   
 1. Extract .zip
 2. Run setup.py

### Manual Install  
 1. Extract .zip
 2. Open a CMD window
 3. Enter each command bellow
>       pip install pyautogui
>       pip install pillow
>       pip install termcolor
>       pip install opencv-python
>       pip install pyyaml
   
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
* 3840x2160 \| Issue with Hero not being selected, select OBYN hero manually as a temporary fix
#### Other Tips:
\| Resolutions based on the above, but are 21:9 may also work  
\| Resolution refers to your main monitor size, not game resolution  
\| This program was designed to work in Windows but should work in other Operating systems

## XP Support
As mentioned this program can automatically gain XP for towers, this is relatively slow, but over a long AFK time it does add up to a lot.  
By default it is not active, to enable this feature edit the config.txt file follow example there.  
All land monkeys are supported for this feature  

## Recording Playthroughs
Not yet fully implemented!!!!
With the file "gameplan_recorder" it is possible to build your own play through that "Py_AutoBloons" will use to beat dark castle!!
This is stored by defualt as "gameplan.csv" and can be specified to use in config.txt, however the "gameplan.csv" will need to be in the same folder as "Py_AutoBloons.py"
Currently auto hero selection only works for Obyn if you would like to use a different hero, disable auto hero select in the config file

If you are interested in recording your own gameplan to beat dark castle, timing is very important, try to give yourself a little extra time before buying upgrades to ensure that on another playthrough you will have enough money to buy the same upgrade.

You should start the recorder once you have loaded in to dark castle, you will have to click the play button in the recording.
You should end the recorder once you see the victory screen, do not click anything once the victory screen loads and give an extra minute or two to account for differances in play throughs
### Insert pictures of start and end 
### Create a video to show how to use it

