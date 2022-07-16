import random


doubles = 0
reset_player = 3

player_list = ["Yellow", "Green", "Red", "Blue"]
print("***********************")
beginning_player = input("Who's going first? (Type 'Yellow', 'Green', 'Red', or 'Blue'):  ")

current_player = int()

while beginning_player != 'Yellow' and beginning_player != 'Green' and beginning_player != 'Red' and beginning_player != 'Blue':
    print("Please enter one of the four colors.")
    beginning_player = input("Who's going first? (Type 'Yellow', 'Green', 'Red', or 'Blue'):  ")

if beginning_player == 'Yellow':
    current_player = 0
elif beginning_player == 'Green':
    current_player = 1
elif beginning_player == 'Red':
    current_player = 2
else:
    current_player = 3


#Should print current player



snake_eyes = 0

player_notified = True

print(f'Player {player_list[current_player]} is up!')

while True:
    for dice in range(1):
        dice_value = random.randint(2, 2)
        dice_value2 = random.randint(2, 2)
        print(f'Your roll was a [{dice_value}] and a [{dice_value2}]')
    if dice_value == 1 and dice_value2 == 1:
        snake_eyes = snake_eyes + 1
        print("Snake Eyes: " + str(snake_eyes))
        if snake_eyes == 3:
            print("YOU WON THE GAME WITH 3 SNAKE EYES! CONGRATULATIONS!")
    if dice_value2 == dice_value:
        doubles = doubles + 1
        if doubles == 3:
            print('')
            print("Doubles:" + str(doubles))
            print('You rolled 3 doubles! Return your farthest player back to home!')
            print('')
            current_player = current_player + 1
            doubles = 0
            if current_player == 4:
                current_player = 0
            print('')
            print(f'Player {player_list[current_player]} is up!')
            doubles = 0
        else:
            print('')
            print('Both dice were the same value! You get another turn!')
            print("Doubles: " + str(doubles))
    else:
        current_player = current_player + 1
        doubles = 0
        if current_player == 4:
            current_player = 0
        print('')
        print(f'Player {player_list[current_player]} is up!')
    input("Press enter to roll: ")