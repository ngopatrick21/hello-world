secret_password = 'kittens'

password = input('Enter the secret password: ')

if password == secret_password:
    print('Welcome, authorized user')

else:
    print('Sorry, wrong password.')

# read_syllabus = input('Enter Y if you read the syllabus for the class: ')
#
#
# if read_syllabus != 'Y':
#     print('Please read the syllabus carefully, there is important info in it. Thanks! ')