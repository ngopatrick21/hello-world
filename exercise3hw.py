import random

number_of_dice = int(input('How many dice to roll?: '))
quit = ''
print(f'About to roll {number_of_dice} dice...')

while not quit:
    for dice in range(1):
        dice_value = random.randint(1, 6)
        dice_value2 = random.randint(1, 6)
        print(f'You rolled a {dice_value} and a {dice_value2}')
    if dice_value2 == dice_value:
        print('Both dice were the same value! You get another turn!')
        input('Press enter to roll again: ')
    else:
        quit = input('Press enter to roll again, any other key to quit: ')