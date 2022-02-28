# Calculate total purchases 
# February 27, 2022
# CTI-110 P2HW1 - Total Purchases
# Angelica Haring
#
# Get prices for five purchased items from user
# Program calculates subtotal of five purchased items prices entered
# Program calculates sales tax of subtotal items prices entered
# Program calculates overall total
# Print Subtotal, Sales Tax, and Total
#
sales_tax = .07
item_num1 = float(input('Enter the price of item #1: '))
item_num2 = float(input('Enter the price of item #2: '))
item_num3 = float(input('Enter the price of item #3: '))
item_num4 = float(input('Enter the price of item #4: '))
item_num5 = float(input('Enter the price of item #5: '))
subtotal = float(item_num1 + item_num2 + item_num3 + item_num4 + item_num5)
total_sales_tax = subtotal * sales_tax
total = subtotal + total_sales_tax
print()
print('-------Results-------')
print('Subtotal: ', format(subtotal, ',.2f'))
print('Sales Tax: ', format(total_sales_tax, ',.2f'))
print('Total: ', format(total, ',.2f'))
