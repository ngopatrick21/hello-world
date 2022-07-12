state = input("What state would you like to be a senator in?: ")
current_state = input("What state do you currently live in?: ")
age = int(input("How old are you?: "))
citizenship = int(input("How long have you been a citizen of the U.S.?: "))

if (age >= 30):
    if (state == current_state) and (citizenship >= 9):
        print("Congratulations! You are eligibile to be a senator in " + str(state))
    elif state != current_state:
        print('You must live in the state youd like to be senator in.')
else:
    print("You are not eligible to be Senator")

