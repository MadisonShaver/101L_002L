'''CS 101 Lab
Program 13
Madison Shaver
mlsy7z@umkc.edu

PROBLEM: Create unit tests to test a program and its functions. 
         The program should find the sum, average, and median of a list of numbers.

ALGORITHM:
    1. Start
    2. Import math module
    3. Calculate total of list of numbers
        3a. set total to 0
        3b. add first number to total
        3c. loop until all numbers are added
        3d. return total
    4. Calculate average of list of numbers
        4a. if the list is empty return nan
        4b. repeat steps 3a-3c
        4c. divide total by number of numbers in list and assign to total
        4d. return total
    5. Calculate median of list of numbers
        5a. sort the list
        5b. if list is empty raise a ValueError
        5c. if length of list is odd, divide length by 2 and round down
        5d. return number of list at calculated index
        5e. if length of list is even, divide length by 2
        5f. divide length by 2 again but subtract 1 this time
        5g. add values add calculated indices
        5h. return added values divided by two (average of two middle numbers)
    6. End
'''

import math

def total(values):
    total = 0
    for i in range(len(values)):
        total += values[i]
    return total

def average(values):
    if len(values) == 0:
        return math.nan
    total = 0
    for i in range(len(values)):
        total += values[i]
    total /= len(values)
    return total

def median(values):
    values.sort()
    if len(values) == 0:
        raise ValueError
    if len(values) % 2 == 1:
        return values[math.floor(len(values) / 2)]
    if len(values) % 2 == 0:
        return (values[len(values) // 2] + values[(len(values) // 2) - 1]) / 2
