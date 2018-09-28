secret = 'Love'

guess = input('Input password: ')
chances = 3

while True:
    if '*' in guess:
        guess = input('Can not contain *, you have {} chances, input again: '.format(chances))
        continue
    elif guess == secret:
        print('Wow~ cool~')
        break
    else:
        chances -= 1
        if chances < 1:
            print('Out!')
        guess = input('Error, you have {} chances: '.format(chances))
