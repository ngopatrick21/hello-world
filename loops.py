# import random
#
# want_to_quit = ''
#
# while not want_to_quit:
#     dice_value = random.randint(1, 6)
#     print(f'You rolled a {dice_value}')
#     want_to_quit = input('Press enter to roll again, any other key to quit: ')

weather = 'snow'
temperature = 29.5
day_of_month = 20

print(f'On January {day_of_month}, the temperature is {temperature} and the current weather is {weather}.')

star_id = input('Enter your StarID: ')

while len(star_id) != 8:
    print('Error - a valid StarID has 8 characters.')
    star_id = input('Please enter your StarID: ')

print(f'Thank you, your StarID is {star_id}')