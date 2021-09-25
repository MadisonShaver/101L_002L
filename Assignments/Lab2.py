'''CS 101 Lab
Program 1
Madison Shaver
mlsy7z@umkc.edu

PROBLEM: Calculating the weighted and letter grade for a student.

ALGORITHM:
    1. Start
    2. output welcome statement
    3. get inputs
        3a. User name
        3b. Labs grade
        3c. Exams grade
        3d. Attendance grade
    4. make sure values are appropriate
        4a. if not, warn user
        4b. change grade to nearest included value
    5. calculate weighted grade
    6. output weighted grade
    7. calculate letter grade
    8. output letter grade
    9. output thanks statement
    10. End'''

def check_grade(grade, name):
    if grade > 100:
        print('The {} value should have been 100 or less. It has been changed to 100.'.format(name))
        grade = 100
    if grade < 0:
        print('The {} value should have been zero or greater. It has been changed to zero.'.format(name))
        grade = 0
    return grade

print('**** Welcome to the LAB grade calculator! ****')
print()
user_name = input('Who are we calculating grades for?\n')

labs_grade = int(input('Enter the Labs grade?\n'))
labs_grade = check_grade(labs_grade, 'lab')
print()

exams_grade = int(input('Enter the Exams grade?\n'))
exams_grade = check_grade(exams_grade, 'exam')
print()

attendance_grade = int(input('Enter the Attendance grade?\n'))
attendance_grade = check_grade(attendance_grade, 'attendance')
print()

weighted_grade = (labs_grade * 0.7) + (exams_grade * 0.2) + (attendance_grade * 0.1)
print('The weighted grade for {0} is {1:.1f}'.format(user_name, weighted_grade))

if weighted_grade >= 90:
    letter_grade = 'A'
elif weighted_grade >= 80:
    letter_grade = 'B'
elif weighted_grade >= 70:
    letter_grade = 'C'
elif weighted_grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'
print('{0} has a letter grade of {1}'.format(user_name, letter_grade))
print()

print('**** Thanks for using the Lab grade calulator ****')