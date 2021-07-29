'''
Login using if, else, elif and print and using time library
'''

import time
# used time library

userName = 'kabir'
passWord = 'password'

usernameInput = input('Enter the Username: ')
passwordInput = input('Password: ')

if usernameInput == userName and passwordInput == passWord:
    print('Access granted')
    print('Please wait')
    time.sleep(5)
    print('Ok... Loading...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print('Alright you have security clearance. Pulling up the secret mainframe.')
elif usernameInput == userName and passwordInput != passWord:
    print('Password incorrect')
elif usernameInput != userName and passwordInput == passWord:
    print('Username incorrect')
else:
    print('You might want to check both fields...')
