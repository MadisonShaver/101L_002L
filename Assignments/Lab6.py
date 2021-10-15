'''CS 101 Lab
Program 6
Madison Shaver
mlsy7z@umkc.edu

PROBLEM:

ALGORITHM:

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