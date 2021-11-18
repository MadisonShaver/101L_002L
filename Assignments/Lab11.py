'''CS 101 Lab
Program 11
Madison Shaver
mlsy7z@umkc.edu

PROBLEM: Get hour, minute, and second and output a ticking clock

ALGORITHM:
    1. Start
    2. Get inputs from user
        2a. hour
        2b. minute
        2c. second
    3. Create an instance of the Clock class with inputted information
        3a. Class should have default values of 0 for hours, minutes, seconds, and clock type
    4. Print instance
        4a. Overload the string function so it will print the clock time
        4b. If the clock type is 0, print a 24 hour clock. If the clock type is 1, 
            print a 12 hour clock with am or pm.
        4c. If the hour is greater than 24, subtract 24 from the hours
        4d. If the hour is 0, rewrite it to be 12
    5. Import time module
    6. Make the clock tick every second and print instance every time it ticks
        6a. If seconds is greater than or equal to 60, add one to minutes and subtract 60 from seconds
        6b. If minutes is greater than or equal to 60, add one to hours and subtract 60 from minutes
    7. End
'''

import time

class Clock():
    def __init__(self, hours = 0, minutes = 0, seconds = 0, clock_type = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.clock_type = clock_type

    def __str__(self):
        if self.hours >= 24:
            self.hours -= 24
        if self.clock_type == 0:
            return '{:02}:{:02}:{:02}'.format(self.hours, self.minutes, self.seconds)
        else:
            if self.hours >= 12:
                if (self.hours - 12) == 0:
                    return '{:02}:{:02}:{:02} pm'.format(12, self.minutes, self.seconds)
                else:
                    return '{:02}:{:02}:{:02} pm'.format(self.hours - 12, self.minutes, self.seconds)
            else:
                if self.hours == 0:
                    return '{:02}:{:02}:{:02} am'.format(12, self.minutes, self.seconds)
                else:
                    return '{:02}:{:02}:{:02} am'.format(self.hours, self.minutes, self.seconds)

    def tick(self):
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        if self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

if __name__ == '__main__':
    hour = int(input('What is the current hour ==> '))
    minute = int(input('What is the current minutes ==> '))
    second = int(input('What is the current second ==> '))
    clock1 = Clock(hour, minute, second, 1)

    while True:
        print(clock1)
        clock1.tick()
        time.sleep(1)