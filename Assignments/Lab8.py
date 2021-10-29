'''CS 101 Lab
Program 8
Madison Shaver
mlsy7z@umkc.edu

PROBLEM: Create a program that adds grades to, removes grades from, and clears lists; 
calculates the weighted and average grade and the standard deviation; 
and displays a menu and the inputted and calculated scores.

ALGORITHM:
    1. Start
    2. Output menu
    3. Get choice from user and proceed based on choice
        3a. add test
            3a.1. get test grade from user
            3a.2. make sure input is valid
            3a.3. add grade to test list
        3b. remove test
            3b.1. get test grade from user
            3b.2. make sure input is valid
            3b.3. remove grade from test list or output warning message if grade not found
        3c. clear test list
        3d. add assignment
            3d.1. get assignment grade from user
            3d.2. make sure input is valid
            3d.3. add grade to assignment list
        3e. remove assignment
            3e.1. get assignment grade from user
            3e.2. make sure input is valid
            3e.3. remove grade from assignment list or output warning message if grade not found
        3f. clear assignment list
        3g. display scores
            3g.1. calculate average grade for tests and assignments
            3g.2. calculate standard deviation for tests and assignments
            3g.3. calculate weighted grade
            3g.4. output grades in a table format
            3g.5. output weighted grade
        3h. quit
    4. If user doesn't choose 'quit', repeat steps 2 and 3 until they do.
    5. End
'''
import math

def print_menu():
    print()
    print('{:^34}'.format('Grade Menu'))
    print('1 - Add Test')
    print('2 - Remove Test')
    print('3 - Clear Tests')
    print('4 - Add Assignment')
    print('5 - Remove Assignment')
    print('6 - Clear Assignments')
    print('D - Display Scores')
    print('Q - Quit')
    print()

def get_input():
    pass

def get_grade(type, func):
    while True:
        print()
        try:
            if func == 'add':
                grade = float(input('Enter the new {} score 0-100 ==> '.format(type)))
            else:
                grade = float(input('Enter the {} to remove 0-100 ==> '.format(type)))
            return grade
        except TypeError:
            print('Grade must be a number.')

def check_grade(grade): 
    while True:
        if grade < 0:
            print('Grade must be greater than or equal to 0.')
            grade = float(input('Try again ==> '))
        else:
            return grade

def add_grade(type):
    grade = get_grade(type, 'add')
    check_grade(grade)
    if type == 'Test':
        tests.append(grade)
    else:
        assignments.append(grade)

def remove_grade(type):
    grade = get_grade(type, 'remove')
    check_grade(grade)
    try:
        if type == 'Test':
            tests.remove(grade)
        else:
            assignments.remove(grade)
    except ValueError:
        print('Could not find that score to remove')

def calc_avg(list):
    avg = 0
    for score in list:
        avg += score
    avg /= len(list)
    return avg

def calc_std(list):
    std = 0
    for score in list:
        std += (score - calc_avg(list)) ** 2
    std = math.sqrt(std / len(list))
    return std

def display_scores():
    print('{:<10}{:>10}{:>10}{:>10}{:>10}{:>10}'.format('Type', '#', 'min', 'max', 'avg', 'std'))
    print('{:=<60}'.format(''))

    if len(tests) == 0:
        print('{:<10}{:>10}{:>10}{:>10}{:>10}{:>10}'.format('Tests', '0', 'n/a', 'n/a', 'n/a', 'n/a'))
    else:
        avg_tests = calc_avg(tests)
        std_tests = calc_std(tests)
        print('{:<10}{:>10}{:>10}{:>10}{:>10.2f}{:>10.2f}'.format('Tests', 
        len(tests), min(tests), max(tests), avg_tests, std_tests))

    if len(assignments) == 0:
        print('{:<10}{:>10}{:>10}{:>10}{:>10}{:>10}'.format('Programs', len(assignments), 'n/a', 'n/a', 'n/a', 'n/a'))
    else:
        avg_assignments = calc_avg(assignments)
        std_assignments = calc_std(assignments)
        print('{:<10}{:>10}{:>10}{:>10}{:>10.2f}{:>10.2f}'.format('Programs', 
        len(assignments), min(assignments), max(assignments), avg_assignments, std_assignments))

    print()
    if len(tests) > 0 and len(assignments) > 0:
        weight = (avg_tests * 0.6) + (avg_assignments * 0.4)
    else: 
        weight = 0

    print('The weighted score is {:.2f}'.format(weight))

if __name__ == '__main__':
    tests = []
    assignments = []
    
    while True:
        print_menu()
        user_choice = input('==> ')

        if user_choice == '1':
            add_grade('Test')
        elif user_choice == '2':
            remove_grade('Test')
        elif user_choice == '3':
            tests = []
        elif user_choice == '4':
            add_grade('Assignment')
        elif user_choice == '5':
            remove_grade('Assignment')
        elif user_choice == '6':
            assignments = []
        elif user_choice.upper() == 'D':
            display_scores()
        elif user_choice.upper() == 'Q':
            break
        else:
            print('Enter a valid option.')