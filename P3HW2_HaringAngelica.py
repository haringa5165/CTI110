# CTI-110
# P3HW2 - Pizza Order
# Angelica Haring
# March 23, 2022
#
# Get the number of students would like to order pizza for from the user
# Get the number of people that will be sharing each pizza from the user
# Program calculates the number of whole pizzas user needs to buy
# Program use ceil function to get the correct number of pizzas
# Program calculates overall total price including sales tax
# Use if-else statement
# Print number of students, pizzas needed, and price including sales tax if true
# Print error message and notify user to enter the valid value and run program again if false
#
import math

students = int(input('How many students do you want to order pizza for? '))
people_per_pizza = float(input('Enter number of people per pizza ( 1.5, 2 or 3): '))
print()

pizzas = math.ceil(students/people_per_pizza)
sales_tax = .06
total = pizzas * 5
total_price = total + (total * sales_tax)

if people_per_pizza == 1.5 or people_per_pizza == 2 or people_per_pizza == 3:
    print('----Pizza Order--------')
    print('Number of Students :', students)
    print('Pizzas Needed :', pizzas)
    print('Price ${:.2F}'.format(total_price))
    print('--------------------------')
else:
    print('INVALID ENTRY!!!!')
    print('Should have entered 1.5, 2 or 3')
    print()
    print('Run Program again')

