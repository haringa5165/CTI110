# CTI-110
# P4HW2 - Pizza Order
# Angelica Haring
# April 7, 2022
#
# Get the number of students would like to order pizza for from the user
# Get the number of people that will be sharing each pizza from the user 
# If user enters a value OTHER than 1.5, 2 or 3, display error and get correct value
# If user enters correct value, program calculates the number of whole pizzas user needs to buy
# Program use ceil function to get the correct number of pizzas
# Program calculates overall total price assuming one pizza costs $5 including sales tax
# Print number of students, pizzas needed, and price including sales tax if correct value
# If user enters incorrect value, print error message and notify user to enter the correct value
# Program asks user if they wish to run the prohram again
# Program only terminates if user chooses not to run the program again
#
import math

print()
students = int(input('How many students do you want to order pizza for? '))
people_per_pizza = float(input('Enter number of people per pizza ( 1.5, 2 or 3): '))
print()
i = 1
userValue = '-'

if people_per_pizza == 1.5 or people_per_pizza == 2 or people_per_pizza == 3:
    pizzas = math.ceil(students/people_per_pizza)
    print('----Pizza Order--------')
    print('Number of Students :', students)
    print('Pizzas Needed :', pizzas)
    total = pizzas * 5
    print('Price ${:.2F}'.format(total + (total * .06)))
    print('--------------------------')
    print()
    print('Would you like to run program again (y for yes): ',end='')
    userValue = input()
    while userValue == 'y' or userValue == 'Y':
        print()
        students = int(input('How many students do you want to order pizza for? '))
        people_per_pizza = float(input('Enter number of people per pizza ( 1.5, 2 or 3): '))
        print()
        if people_per_pizza == 1.5 or people_per_pizza == 2 or people_per_pizza == 3:
            pizzas = math.ceil(students/people_per_pizza)
            print('----Pizza Order--------')
            print('Number of Students :', students)
            print('Pizzas Needed :', pizzas)
            total = pizzas * 5
            print('Price ${:.2F}'.format(total + (total * .06)))
            print('--------------------------')
            print()
            print('Would you like to run program again (y for yes): ',end='')
            userValue = input()
        else:
            print('INVALID ENTRY!!!!')
            print('Should have entered 1.5, 2 or 3')
            print()
            people_per_pizza = float(input('Enter number of people per pizza again.( 1.5, 2 or 3): '))
            if people_per_pizza == 1.5 or people_per_pizza == 2 or people_per_pizza == 3:
                pizzas = math.ceil(students/people_per_pizza)
                print()
                print('----Pizza Order--------')
                print('Number of Students :', students)
                print('Pizzas Needed :', pizzas)
                total = pizzas * 5
                print('Price ${:.2F}'.format(total + (total * .06)))
                print('--------------------------')
                print()
                print('Would you like to run program again (y for yes): ',end='')
                userValue = input()
        if userValue != 'y' or userValue != 'Y':
            print('Good Bye!')
else:
    print('INVALID ENTRY!!!!')
    print('Should have entered 1.5, 2 or 3')
    print()
    people_per_pizza = float(input('Enter number of people per pizza again.( 1.5, 2 or 3): '))
    if people_per_pizza == 1.5 or people_per_pizza == 2 or people_per_pizza == 3:
            pizzas = math.ceil(students/people_per_pizza)
            print()
            print('----Pizza Order--------')
            print('Number of Students :', students)
            print('Pizzas Needed :', pizzas)
            total = pizzas * 5
            print('Price ${:.2F}'.format(total + (total * .06)))
            print('--------------------------')
            print()
            print('Would you like to run program again (y for yes): ',end='')
            userValue = input()
            while userValue == 'y' or userValue == 'Y':
                print()
                students = int(input('How many students do you want to order pizza for? '))
                people_per_pizza = float(input('Enter number of people per pizza ( 1.5, 2 or 3): '))
                print()
                if people_per_pizza == 1.5 or people_per_pizza == 2 or people_per_pizza == 3:
                    pizzas = math.ceil(students/people_per_pizza)
                    print('----Pizza Order--------')
                    print('Number of Students :', students)
                    print('Pizzas Needed :', pizzas)
                    total = pizzas * 5
                    print('Price ${:.2F}'.format(total + (total * .06)))
                    print('--------------------------')
                    print()
                    print('Would you like to run program again (y for yes): ',end='')
                    userValue = input()
                else:
                    print('INVALID ENTRY!!!!')
                    print('Should have entered 1.5, 2 or 3')
                    print()
                    people_per_pizza = float(input('Enter number of people per pizza again.( 1.5, 2 or 3): '))
            if userValue != 'y' or userValue != 'Y':
                    print('Good Bye!')

