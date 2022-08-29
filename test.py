import csv, time
from typing import final





def time_sleep_calc(delay):

    #Here we handle the hour portion of the delay
    hours = delay[0]
    #print("hours = ", hours)
    convert_hours = int(hours) * 60 * 60

    #Here we handle the minute portion of the delay
    tuple_minutes = delay[2], delay[3]
    minutes = ''.join(str(x) for x in tuple_minutes)
    #print("minutes = ", minutes)
    convert_minutes = int(minutes) * 60

    #Here we handle the second portion of the delay
    tuple_seconds = delay[5], delay[6]
    seconds = ''.join(str(x) for x in tuple_seconds)
    #print("seconds = ", seconds)

    #Then we add all the converted seconds together
    final_delay = int(seconds) + convert_minutes + convert_hours
    print(final_delay)

    time.sleep(final_delay)

def Main_Game_Reader():

    gameplanArray = []
    gameplanFile = "2.csv"
    with open(gameplanFile, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')


        for row in spamreader: 
            gameplanArray.append(row) # We build an array of the list in each row
            # This is used as to not keep the file open in case of a program crash..

    #print(gameplanArray)

    for line in gameplanArray:
        if "Resolution" in line[0]:
            resolution = line[2] + " " + line[3]
            print(resolution)
            pass

       

        if line[0] == "Keyboard ":
            key = line[2]
            delay = line[1]


            print(key + " " + delay)
            
            time_sleep_calc(delay)
            pass
        

        if line[0] == "Click ":
            location = line[2]
            delay = line[1]
            print(location + " " + delay)

            time_sleep_calc(delay)
            pass
        

        

Main_Game_Reader()