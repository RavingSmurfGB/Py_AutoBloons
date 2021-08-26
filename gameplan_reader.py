import csv

gameplanArray = []


with open('gameplan.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        
        time = row[0]
        updown = row[1]
        location = row[2]
        print(time, updown, location)


        