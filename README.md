# Py_AutoBloons
A Python script that will beat Bloons TD 6 on Dark Castle

## Contents
* [How It Works](#How_It_Works)
* [Installation](#Installation)
* [How To Use](#How_To_Use)
* [What Is Needed](#What_Is_Needed)
* [Compatibility](#Compatibility)
* [XP Support](#XP_Support)

### How It Works
This program will select the map Dark Castle, beat it on easy difficulty, collect any levels, collect any event items, then loop continously.  
It will use the Hero OBYN (Which will be selected auto if not), a submarine and a ninja monkey to beat the gane.  
Please view [What Is Needed](#What_Is_Needed)<a name="What_Is_Needed"></a> to ensure your setup and ready to run the program.  
Please view [XP Support](#XP_Support)<a name="XP_Support"></a> if you would like this program to automate XP gathring for monkeys.


### Installation
#### Automatic Install   
 1. Extract .zip
 2. Run setup.py

#### Manual Install  
 1. Extract .zip
 2. Open a CMD window
 3. Enter each command bellow
>       pip install pyautogui
>       pip install pillow
>       pip install termcolor
>       pip install opencv-python
>       pip install pyyaml
   
### How To Use
 1. Launch Bloons TD 6
 2. Double click Py_AutoBloons.py
 3. Tab back in to Bloons TD 6 within 5 seconds / ensure your cursor is over it   
 \| The Bloons TD 6 Game must be played on your primary monitor.

### What Is Needed
To run this script ensure that the following upgrades are obtained and the Expert map Dark Castle is unlocked.
Monkey        | Upgrade
------------- | -------------
Submarine     | <ul><li>Longer Range</li><li>Advanced Intel</li><li>Twin Guns</li><li>Airburst Darts</li><li>Triple Guns</li><li>Armor Piercing Darts</li>
Ninja         | <ul><li>Ninja Discipline</li><li>Sharp Shurikens</li><li>Double Shot</li><li>Seeking Shuriken</li>


### Compatibility
#### Resolutions officialy supported:  
* 1920x1080  
* 2560x1440  
* 3840x2160 \| Not yet fully implemented  
#### Other Tips:
\| Resolutions based on the above, but are 21:9 may also work  
\| Resolution refers to your main monitor size, not game resolution  
\| This program was designed to work in Windows but should work in other Operating systems

### XP Support
As mentioned this program can automatically gain XP for towers, this is relatively slow, but over a long AFK time it does add up to a lot.
By default it is not active, to enable this feature edit the config.txt file follow example there.
All land monkeys are supported for this feature
