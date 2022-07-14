import random

number_of_dice = int(input('How many dice to roll?: '))

print(f'About to roll {number_of_dice} dice...')

for dice in range(number_of_dice):
    dice_value = random.randint(1, 6)
    print(dice_value)