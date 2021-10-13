'''CS 101 Lab
Program 5
Madison Shaver
mlsy7z@umkc.edu

PROBLEM: Creating a library card check. It will tell whether the card is valid or invalid and why if it is invalid.

ALGORITHM:
    1. Start
    2. print header
    3. get input
        3a. user's card number
    4. check to make sure card is valid
        4a. card number is length 10
        4b. first five characters are letters
        4c. sixth digit is 1, 2, or 3
        4d. seventh digit is 1, 2, 3, or 4
        4e. eigth, ninth, and tenth digits are all numbers from 0-9
        4f. check digit is correct
            4f.1. get numbers that represents the letters (A - 0, B - 1, ... Z - 25)
            4f.2. calculate check digit ((index * number) + (index * number)...)
    5. print whether or not the card is valid
    6. print additional statements
        6a. if card is valid, print school and grade student is in
            6a.1. sixth digit represents school
            6a.2. seventh digit represents grade
        6b. if card is invalid, print why
    7. repeat steps 3 - 6 if user wants to play again
    8. End'''

def get_school(num):
    '''Returns school based on number at index 5 of card #. Returns False if number is greater than 3.'''
    schools = {1:'School of Computing and Engineering SCE', 2:'School of Law', 3:'College of Arts and Sciences'}
    if 0 < num <= 3:
        return schools[num]
    else:
        return False

def get_grade(num):
    '''Returns grade based on number at index 6 of card #. Returns false is number is greater than 4.'''
    grades = {1:'Freshman', 2:'Sophomore', 3:'Junior', 4:'Senior'}
    if 0 < num <= 4:
        return grades[num]
    else:
        return False

def character_value(letter):
    '''Returns the number assigned to each letter. A - 0, B - 1, ... Z - 25.'''
    result = ord(letter) - 65
    return result

def get_check_digit(card_num):
    '''Returns the correct check digit for the card # given.'''
    result = 0
    for i in range(0, 9):
        result += (character_value(card_num[i]) * (i + 1))
    return result % 10

def verify_check_digit(card_num):
    '''Returns False and statement why card is invalid if it is invalid, returns true if it is valid.'''
    if len(card_num) != 10:
        return False, "The length of the number given must be 10"

    for i in range(0, 5):
        if not card_num[i].isalpha():
            return False, "The first 5 characters must be A-Z, the invalid character is at {0} is {1}".format(i, card_num[i])

    for i in range(7, 10):
        if not card_num[i].isdigit():
            return False, "The last 3 characters must be 0-9, the invalid character is at {0} is {1}".format(i, card_num[i])

    if card_num[5] != '1' and card_num[5] != '2' and card_num[5] != '3':
        return False, "The sixth character must be 1, 2, or 3"

    if card_num[6] != '1' and card_num[6] != '2' and card_num[6] != '3' and card_num[6] != '4':
        return False, "The seventh character must be 1, 2, 3, or 4"

    if int(card_num[9]) != get_check_digit(card_num):
        return False, "Check digit {0} does not match calculated value {1}".format(card_num[9], get_check_digit(card_num))

    return True, ""

if __name__ == '__main__':
    print('{:^60}'.format('Linda Hall'))
    print('{:^60}'.format('Library Card Check'))
    print('{:=^60}'.format(''))

    while True:
        print()
        user_card = input('Enter Library Card.  Hit Enter to Exit ==> ')

        if user_card == '':
            break

        validity, reason = verify_check_digit(user_card)

        if validity == True:
            print('Library card is valid.')

            school = get_school(int(user_card[5]))
            grade = get_grade(int(user_card[6]))

            print('The card belongs to a student in {}'.format(school))
            print('The card belongs to a {}'.format(grade))
        else:
            print('Library card is invalid.')
            print(reason)