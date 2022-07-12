pennies = float(input("How many pennies do you have?: "))

if pennies < 100:
    print('You have less than a dollar.')
elif pennies == 100:
    print('You have exactly one dollar.')
elif pennies > 100:
    print('You have more than one dollar.')
else:
    print('')
