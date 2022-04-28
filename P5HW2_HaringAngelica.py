# Program answer the math quiz
# April 28, 2022
# CTI-110 P5HW2 - Math Quiz
# Angelica Haring
#
# Create the program a Menu Driven, asking user to make a choice from list of options
# Create a program that display two random numbers
# Create a function to add and subtract the random numbers
# Get answer from the random numbers from the user
# Evaluate every choice entered if valid, should be 1, 2, or 3
# If invalid, allows the user to enter the valid option
# If incorrect answer, program to show guess is not correct and show the correct answer
# If correct answer, congratulate the user showing answer is correct
# Let the user answer math quizzes again and again until the user exit the program, choosing 3 from the option
#
import random
print('Welcome to Math Quiz')
print('')

def add_random():
    num_one = random.randint(0,100)
    num_two = random.randint(0,100)
    print(' ',num_one)
    print('+',num_two)
    sum=num_one+num_two
    print('')
    ans=int(input('Enter answer.\n'))
    if sum!=ans:
        print('Sorry, your guess is not correct.')
        print('The correct answer is', sum)
    else:
        print('Congratulations!!!! Your answer is correct.')
        
def sub_random():
    num_one = random.randint(0,100)
    num_two = random.randint(0,100)
    print(' ',num_one)
    print('-',num_two)
    diff=num_one-num_two
    print('')
    ans=int(input('Enter answer.\n'))
    if diff!=ans:
        print('Sorry, your guess is not correct.')
        print('The correct answer is', diff)
    else:
        print('Congratulations!!!! Your answer is correct.')
if __name__=="__main__":
    
    while True:
        print('')
        print('MAIN MENU')
        print('--------------------')
        print('1. Adding Random Numbers')
        print('2. Subtracting Random Numbers')
        print('3. Exit')
        print('')
        user_input = int(input('Please choose one of the menu options: '))
        if user_input==3:
            print('Thank you for playing...')
            print('Bye!!')
            break
        elif user_input==1:
            add_random()
        elif user_input==2:
            sub_random()
        else:
            print('This is not an option for this menu.')
            print('Please enter 1, 2, or 3.')    

