# These will calculate number of pizzas needed to order for a group of students and total slices of pizza. There are 6 slices per pizza and each student gets 3 slices. 
# February 15, 2022
# CTI-110 P1HW2 - Pizza Order
# Angelica Haring

students = int(input('How many students do you want to order pizza for? '))
print()
slices = students * 3
pizza = students / 2

print('----Pizza Order--------')
print('Number of Students :', students) # number of students entered
print('Pizza Slices Needed:', slices) # number of pizza slices
print('Pizzas Needed :', pizza) # number of pizzas needed
print('--------------------------')
