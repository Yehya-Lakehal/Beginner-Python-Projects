# This module let us work with Time!
import time

print("Welcome to my Timer!")

mytime = int(input("Enter time in seconds: "))

for i in range(mytime, 0, -1):
    secs = i % 60
    mins = (i // 60) % 60
    hours = (i // 3600) % 24
    print(f"{hours:02}:{mins:02}:{secs:02}")
    time.sleep(1)

print("TIME IS OVER!")