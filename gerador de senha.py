from time import sleep
from random import choice
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
simbols = ['@','#','$']

print('+='* 40)
print('PASSWORD GENERATOR')
print('+='* 40)
while True :
    click_here = str(input('Press enter to generate your password: '))

    if click_here != '1':
        print (' press key 1')
    elif click_here == '1':
        break

print('loading...')
sleep(2)
password1 = choice(characters)
password2 = choice(characters)
password3 = choice(characters)
password4 = choice(characters)
password5 = choice(characters)
password6 = choice(characters)
password7 = choice(characters)
password8 = choice(simbols)
allPass = (password1 + password2 + password3 + password4 + password5  + password6 + password7 + password8).upper()
print(f'Here is your password {allPass }.')
