from datetime import datetime
bloons_start_time = 1
auto_restart_period = 2
time_now = 5


#time_addition = int(datetime.now().strftime("%H")) + bloons_start_time # We add the current time and when bloons TD started together
#if time_addition >= auto_restart_period:
    #print("time is now" , datetime.now().strftime("%H"))
    
    #print("we should restart bloons")



if time_now - bloons_start_time >= auto_restart_period:
    print("we should restart bloons")
