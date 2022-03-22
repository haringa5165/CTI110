# Debug the program
# March 22, 2022
# CTI-110 P3H1 - Debugging
# Angelica Haring
#
# This program takes a number grade and outputs a letter grade.
# system uses 10-point grading scale
# Ask user to input grade
# Write branching using the if-else statement
# Print equivalent letter grade
#

A_score = 90
B_score = 80
C_score = 70
D_score = 60
F_score = 50

score = float(input('Please enter grade: '))

def main():

    if score >= A_score:
        print('Grade is A.')
    elif score >= B_score:
        print('Grade is B.')
    elif score >= C_score:
        print('Grade is C.')
    elif score >= D_score:
        print('Grade is D.')
    else:
        print('Grade is F.')

main()
