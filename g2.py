import random
num = random.randint(1, 100)
guess = int(input('guess number 1-100: '))

while guess > num:
    if guess > num:
        print('too high')
    if guess < num:
        print('too low')
    guess = int(input('try again:'))
print('you guessed it')