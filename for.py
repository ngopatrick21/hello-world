# # for number in range(100):
# #     print(number)
# import random
#
# number_of_dice = int(input('How many dice to roll?: '))
#
# print(f'About to roll {number_of_dice} dice...')
#
# for dice in range(number_of_dice):
#     dice_value = random.randint(1, 6)
#     print(f'Dice {dice+1} value is {dice_value}')

# name = 'Patrick'
#
# for letter in name:
#     print(letter)

# square_size = 10
# square_character = '*'
#
# for y in range(square_size):
#     line = ''
#     for x in range(square_size):
#         line = line + square_character
#     print(line)

# name = 'Patrick'
# name_builder = ''
#
# for letter in name:
#     print(name_builder + letter)
#     name_builder = name_builder + letter


name = input('What is your name?: ')
count = len(name)

for letter in name:
    line = ''
    for i in range(count - (len(name) - 1)):
        line = line + letter

    print(line)
    count = count + 1

# for letter in range(len(name)):
#     letter_number = int(letter)
#     for i in range(letter + 1):
#         print(letter, end='')
#     print('')

# rows = 5
# for i in range(rows + 1):
#     for j in range(i):
#         print(i, end='')
#     print('')


# name_builder = name_builder + letter
