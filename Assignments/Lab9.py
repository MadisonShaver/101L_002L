'''CS 101 Lab
Program 9
Madison Shaver
mlsy7z@umkc.edu

PROBLEM: Get file and output information from that file about crimes and how many times those crimes were commited.

ALGORITHM:
    1. Start
    2. Get file from user
        2a. use exception handling to ensure the file is valid
    3. Open file
    4. Create list from csv file
    5. Close file
    6. Output month with highest number of offenses
        6a. create a new date dictionary
        6b. iterate through file starting on the second line
            6a.1. if date is found in new date dictionary, increment correlating value
            6a.2. if not, create new dictionary with date as key and 1 as value
        6c. split the date to just get the month the offense occured
        6d. create new dictionary for month
        6e. iterate through new date dict
            6e.1. if month found in new month dict, add the new date value
            6e.2. if not, create new entry with month as key, and the number from date dict as the value
        6f. find max value in new month dict and corresponding month
        6g. output value and month
    7. Output offense with highest number of crimes
        7a. create new offense dict
        7b. iterate through crime file starting on the second line
            7b.1. if offense found in new offense dict, increment correlating value
            7b.2. if not, create new entry with offense as key and 1 as value
        7c. find max value and corresponding offense
        7d. output max value and offense
    8. Create an offense by zip code dictionary
        8a. iterate through crime file starting on the second line
        8b. if offense is not found in offense by zip dict, create empty entry with offense as key
        8c. if zip is found in offense by zip dict under the offense entry, increment zip entry
        8d. if zip not found in offense by zip dict, create new entry with zip as key and 1 as value
    9. Get an offense from user
        9a. use exception handling to make sure offense is found in offense by zip code dictionary
    10. Use the offense by zip code dictionary and the user chosen offense to output a table of zip 
        codes and how many times that offense was commited in the zip code
    11. End 
'''

import csv

def month_from_number(month_num):
    months = {1:'January', 
              2:'February', 
              3:'March', 
              4:'April', 
              5:'May', 
              6:'June', 
              7:'July', 
              8:'August', 
              9:'September', 
              10:'October', 
              11:'November', 
              12:'December'
              }
    return months[month_num]

def read_in_file(file_name):
    file_list = []
    file = open(file_name, encoding="utf-8")
    file_csv = csv.reader(file)
    for line in file_csv:
        file_list.append(line)
    file.close()
    return file_list

def create_reported_date_dict(crime_list):
    crimes_per_date = {}
    for line in crime_list[1:]:
        if line[1] in crimes_per_date:
            crimes_per_date[line[1]] += 1
        else:
            crimes_per_date[line[1]] = 1
    return crimes_per_date

def create_reported_month_dict(crime_list):
    crimes_per_month = {}
    crimes_per_date = create_reported_date_dict(crime_list)
    for date in crimes_per_date:
        sep_date = date.split('/')
        month = int(sep_date[0])
        if month in crimes_per_month:
            crimes_per_month[month] += crimes_per_date[date]
        else:
            crimes_per_month[month] = crimes_per_date[date]
    return crimes_per_month

def create_offense_dict(crime_list):
    crimes_per_offense = {}
    for line in crime_list[1:]:
        if line[7] in crimes_per_offense:
            crimes_per_offense[line[7]] += 1
        else:
            crimes_per_offense[line[7]] = 1
    return crimes_per_offense

def create_offense_by_zip(crime_list):
    offense_by_zip = {}
    for line in crime_list[1:]:
        offense = line[7]
        zip = line[13]
        if offense not in offense_by_zip:
            offense_by_zip[offense] = {}
        if zip in offense_by_zip[offense]:
            offense_by_zip[offense][zip] += 1
        else:
            offense_by_zip[offense][zip] = 1
    return offense_by_zip

if __name__ == '__main__':
    while True:
        crime_file = input('Enter the name of the crime data file ==> ')
        try:
            crime_list = read_in_file(crime_file)
            break
        except FileNotFoundError:
            print('Could not find the file specified. {} not found'.format(crime_file))
    print()
    
    crimes_per_month = create_reported_month_dict(crime_list)
    max_crime_month = max(crimes_per_month.values())
    for key in crimes_per_month:
        if crimes_per_month[key] == max_crime_month:
            max_month = key
    max_month = month_from_number(max_month)
    print('The month with the highest number of crimes is {0} with {1} offenses'.format(max_month, max_crime_month))

    crimes_per_offense = create_offense_dict(crime_list)
    max_offense_num = max(crimes_per_offense.values())
    for key in crimes_per_offense:
        if crimes_per_offense[key] == max_offense_num:
            max_offense = key
    print('The offense with the highest number of crimes is {0} with {1} offenses'.format(max_offense, max_offense_num))

    while True:
        print()   
        user_offense = (input('Enter an offense ==> ')).capitalize()
        offense_by_zip = create_offense_by_zip(crime_list)
        if user_offense in offense_by_zip:
            print()
            print('{} offenses by Zip Code'.format(user_offense))
            print('{:<15}{:>15}'.format('Zip Code', '# Offenses'))
            print('{:=<30}'.format(''))
            for zip in offense_by_zip[user_offense]:
                print('{:<15}{:>15}'.format(zip, offense_by_zip[user_offense][zip]))
            break
        else:
            print('Not a valid offense found, please try again')