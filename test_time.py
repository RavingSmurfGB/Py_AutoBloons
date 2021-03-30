import time
from datetime import datetime

dt_string1 = datetime.now().strftime("%H:%M:%S")
print(dt_string1)
time.sleep(2)

dt_string2 = datetime.now().strftime("%H:%M:%S")
print(dt_string2)

FMT = '%H:%M:%S'

# we must specify the 2nd time first, so it knows that to take away
tdelta = datetime.strptime(dt_string2, FMT) - datetime.strptime(dt_string1, FMT)
print(tdelta)