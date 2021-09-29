'''CS 101 Lab
Program 3
Madison Shaver
mlsy7z@umkc.edu

PROBLEM: Creating a number guesser based on the number's remainder when divided by 3, 5, and 7.

ALGORITM:
    1. Start
    2. output welcome statement
    3. output prompt to think of number between 1-100
    4. get inputs
        4a. remainder of number when divided by 3
        4b. remainder when divided by 5
        4c. remainder when divided by 7
    5. make sure values are appropriate
        5a. if not, get new input from user
    6. find number from 1-100 with same remainders as user's number
    7. output number
    8. output 'How amazing is that?'
    9. ask user if they want to play again
        9a. if they do, repeat steps 3-9
    10. End'''

def check_value(value, upper_thres):
    '''Make sure values are appropriate for program.'''
    if value < 0:
        print('The value entered must be 0 or greater')
    if value >= upper_thres:
        print('The value entered must be less than', upper_thres)
    return value

print('Welcome to the Flarsheim Guesser!')
cont = 'y'

while cont == 'y':
    print()
    print('Please think of a number between and including 1 and 100.')
    print()

    remain3 = int(input('What is the remainder when your number is divided by 3?'))
    while remain3 not in range(0, 3):
        remain3 = check_value(remain3, 3)
        remain3 = int(input('What is the remainder when your number is divided by 3?'))

    print()
    remain5 = int(input('What is the remainder when your number is divided by 5?'))
    while remain5 not in range(0, 5):
        remain5 = check_value(remain5, 5)
        remain5 = int(input('What is the remainder when your number is divided by 5?'))

    print()
    remain7 = int(input('What is the remainder when your number is divided by 7?'))
    while remain7 not in range(0, 7):
        remain7 = check_value(remain7, 7)
        remain7 = int(input('What is the remainder when your number is divided by 7?'))

    for n in range(1, 101):
        if (n % 3 == remain3) and (n % 5 == remain5) and (n % 7 == remain7):
            print('Your number was', n)
            print('How amazing is that?')
            print()
            break
    else:
        print('You chose an invalid number.')
        print()

    cont = input('Do you want to play again? Y to continue, N to quit')
    while cont != 'y':
        if cont == 'n':
            break
        else:
            cont = input('Do you want to play again? Y to continue, N to quit')