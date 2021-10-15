'''CS 101 Lab
Program 6
Madison Shaver
mlsy7z@umkc.edu

PROBLEM: Caesar encryption/decryption with given key.

ALGORITHM:
    1. Start
    2. print menu options
    3. get choice from user (encrypt, decrypt, or quit)
    4. Continue based on choice
        4a. encryption
            4a.1. get phrase from user
            4a.2. get key from user
            4a.3. use the ord() function to shift each letter the number of times as the given key
            4a.4. output encrypted message
        4b. decryption
            4b.1. get phrase from user
            4b.2. get key from user
            4b.3. use the ord() function to shift each letter backwards the number of times as the given key
            4b.4. output decrypted message
        4c. quit     
    5. Loop steps 2 - 4 until user quits
    6. End
'''

import string

def encrypt(phrase, key):
    '''Caesar-encrypts string using specified key.'''
    new_phrase = ''
    for char in phrase.upper():
        if char != ' ':
            char = chr(ord(char) + key)
        new_phrase += char
    return new_phrase

def decrypt(phrase, key):
    '''Decrypts Caesar-encrypted string with specified string.'''
    message = encrypt(phrase, (key * -1))
    return message

def get_input():
    user_input = input('Enter your selection ==> ')
    while (user_input != '1') and (user_input != '2') and (user_input != 'Q'):
        print('You must enter 1, 2, or Q.')
        user_input = input('Enter your selection ==> ')
    return user_input

def print_menu():
    print('MAIN MENU:')
    print('1) Encode a string')
    print('2) Decode a string')
    print('Q) Quit')


if __name__ == '__main__':
    while True:
        print_menu()
        choice = get_input()
        print()
        if choice == '1':
            orig_message = input('Enter (brief) text to encrypt: ')
            key = int(input('Enter the number to shift letters by: '))
            new_message = encrypt(orig_message, key)
            print('Encrypted:', new_message)
        elif choice == '2':
            orig_message = input('Enter (brief) text to decrypt: ')
            key = int(input('Enter the number to shift letters by: '))
            new_message = decrypt(orig_message, key)
            print('Decrypted:', new_message)
        else:
            break
        print()