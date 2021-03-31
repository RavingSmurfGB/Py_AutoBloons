import time
from datetime import datetime








seconds_before = time.time()
print("Seconds  =", seconds_before)	

time.sleep(2)

seconds_after = time.time()
print("Seconds now  =", seconds_after)

time_dif = seconds_after - seconds_before

print(time_dif)

time_dif = -1

if time_dif < 0:
    print("caught minus")
    print(time_dif)
    time_dif = 0
print(time_dif)
time.sleep(time_dif)

print("we made it thorught")





'''
FMT = '%H:%M:%S'

dt_string1 = datetime.now().strftime("%H:%M:%S")
print(dt_string1)
time.sleep(1)

dt_string2 = datetime.now().strftime("%H:%M:%S")
print(dt_string2)



# we must specify the 2nd time first, so it knows that to take away
#tdelta = datetime.strptime(dt_string2, FMT) - datetime.strptime(dt_string1, FMT)

tdelta = datetime.strptime(dt_string1, FMT) - datetime.strptime(dt_string2, FMT)

print(tdelta)



if tdelta.total_seconds() < 0:
    print("caught minus")
    print(tdelta)
    
    #tdelta = 0
    tdelta = datetime.fromtimestamp(0).strftime(FMT)
    print(tdelta)

#print(tdelta.total_seconds())

'''

