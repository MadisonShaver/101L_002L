'''CS 101 Lab
Program 7
Madison Shaver
mlsy7z@umkc.edu

PROBLEM: Opening a requested file and outputing all vehicles with mpg greater than given by user to another file.

ALGORITHM:
    1. Start
    2. Get minimum mpg
        2a. Loop until given valid input (between 0 and 100)
    3. Get input file
        3a. Use exception handling if file is invalid
        3b. Loop until given valid input
    4. Get output file
        4a. Use exception handling if file is invalid
        4b. Loop until given valid input
    5. Open input and output files
    6. Use for loop to retrieve all vehicles with combined mpg equal to or greater than given minimum mpg
    7. Output to given output file
    8. If invalid values in input file, use exception handling
        7a. Output exceptions
    9. Close input and output files
    10. End
'''

def get_min_mpg():
    '''Returns user entered min mpg value after making sure it is valid.'''
    while True:
        try:
            user_mpg = int(input('Enter the minimum mpg ==> '))

            if user_mpg <= 0:
                print('Fuel economy given must be greater than 0')
            elif user_mpg >= 100:
                print('Fuel economy given must be less than 100')
            else:
                return user_mpg

        except ValueError:
            print('You must enter a number for the fuel economy')

def open_file(str, mode):
    '''Takes input prompt and mode, and opens the requested file.'''
    while True:
        try:
            user_file = input(str)
            return open(user_file, mode)
        except FileNotFoundError:
            print('Could not open file {}'.format(user_file))
        except IOError:
            print('There is an IO Error {}'.format(user_file))

if __name__ == '__main__':
    mpg = get_min_mpg()

    print()
    input_file = open_file('Enter the name of the input vehicle file ==> ', 'r')
    input_file.readline()
    print()
    output_file = open_file('Enter the name of the file to output to ==> ', 'w')
    print()

    for line in input_file:
        info = line.split('\t')

        try:
            ttl_mpg = int(info[7])
            if ttl_mpg >= mpg:
                output_file.write('{:<5}{:<20}{:<40}{:>10.3f}'.format(info[0], info[1], info[2], ttl_mpg))
        except ValueError:
            print('Could not convert value {0} for vehicle {1} {2} {3}'.format(info[7], info[0], info[1], info[2]))

    input_file.close()
    output_file.close()