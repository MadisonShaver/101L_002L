'''CS 101 Lab
Program 4
Madison Shaver
mlsy7z@umkc.edu

PROBLEM: Creating a slots game using functions.

ALGORITHM:
    1. Start
    2. Create variables
        2a. bank (ask user for input. If out of expected range, warn user and ask again)
        2b. initial bank
        2c. spins
        2d. max chips
    3. Get input
        3a. wager (ask user for input. If out of expected range, warn user and ask again)
    4. Spin the slot machine - randomly generated numbers
    5. Find how many reels match
    6. Calculate payout based on matches and wager
    7. Increase bank by payout
    8. Increment spins by one
    9. Output variables
        9a. reels
        9b. matches
        9c. payout
        9d. bank
    10. If bank is greater than max chips, set max chips equal to bank
    11. Repeat steps 3 - 10 if there is more than 0 chips in bank
    12. Output more variables
        12a. initial bank
        12b. spins
        12c. max chips
    13. Ask user if they want to play again
        13a. if they do, repeat steps 2 - 12
    14. End
'''

import random

def play_again():
    '''Asks user if they want to play again, returns False if N or NO, and True if Y or YES.'''
    while True:
        user_play = input('Do you want to play again?')
        if (user_play.upper() == 'YES') or (user_play.upper() == 'Y'):
            return True
        elif (user_play.upper() == 'NO') or (user_play.upper() == 'N'):
            return False
        else:
            print()
            print('You must enter Y/YES/N/NO to continue. Please try again.')

def get_wager(bank):
    '''Asks user for a wager amount. Countines to ask if the result is <= 0 or greater than the amount in their bank.'''
    while True:
        user_wager = int(input('How many chips would you like to wager?'))
        if user_wager < 0:
            print()
            print('The wager amount must be greater than 0. Please enter again.')
        elif user_wager > bank:
            print()
            print('The wager amount cannot be greater than how much you have.', bank)
        else:
            return user_wager

def get_slot_results():
    '''Returns the result of the slot pull.'''
    reel1 = random.randint(1, 10)
    reel2 = random.randint(1, 10)
    reel3 = random.randint(1, 10)
    return (reel1, reel2, reel3)

def get_matches(reela, reelb, reelc):
    '''Returns 3 if all are the same, 2 if there is a match, and 0 otherwise.'''
    reels = [reela, reelb, reelc]
    total_matches = 0
    for i in range(1, 10):
        matches = reels.count(i)
        if total_matches < matches:
            total_matches = matches
    if total_matches == 1:
        return 0
    return total_matches

def get_bank():
    '''Returns how many chips the player wants to play with. Must be between and including 1 and 100.'''
    while True:
        user_bank = int(input('How many chips do you want to start with?'))
        if user_bank <= 0:
            print()
            print('Too low a value, you can only choose 1 - 100 chips')
        elif user_bank > 100:
            print()
            print('Too high a value, you can only choose 1 - 100 chips')
        else:
            return user_bank
    
def get_payout(wager, matches):
    '''Returns the payout amount. 10 times wager if 3 matches, 3 times wager if 2, negative wager if 0.'''
    if matches == 3:
        payout = (10 * wager) - wager
    if matches == 2:
        payout = (3 * wager) - wager
    if matches == 0:
        payout = -wager
    return payout

if __name__ == '__main__':
    playing = True
    while playing:
        bank = get_bank()
        init_bank = bank
        spins = 0
        max_chips = bank
        
        while bank > 0:
            wager = get_wager(bank)
            reel1, reel2, reel3 = get_slot_results()
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            spins += 1

            print('Your spin', reel1, reel2, reel3)
            print('You matched', matches, 'reels')
            print('You won/lost', payout)
            print('Current bank', bank)
            print()

            if bank > max_chips:
                max_chips = bank

        print('You lost all {0} in {1} spins.'.format(init_bank, spins))
        print('The most chips you had was', max_chips)
        playing = play_again()