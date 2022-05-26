#!/usr/bin/python3
#A.R. 20220526v1
#import date and time

from datetime import datetime

now = datetime.now()

#UTC time
current_time = now.strftime("%H:%M:%S")

#print UTC time to screen
print("Current UTC Time =", current_time)
