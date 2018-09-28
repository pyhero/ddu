import random

# define guess zone by GM
number_min = 1
number_max = 9

# generate secret
secret_pool = [x for x in range(number_min, number_max + 1)]
secret = random.choice(secret_pool)

# get guess chances by player
chances_input = input('Guess number game, how many chances do you want: ')
while not chances_input.isdigit():
    chances_input = input('type error, only support int: ')
chances = int(chances_input)

chance_max = number_max - number_min + 1
while (chances < 1) or (chances > chance_max):
    chances = int(input('chose from 1-{}: '.format(chance_max)))

# get guess number by player
guess_input = input('Guess the number({}-{}, {} chances): '.format(number_min, number_max, chances))
while not guess_input.isdigit():
    guess_input = input('type error, only support int: ')
guess = int(guess_input)

chances -= 1
while (guess < number_min) or (guess > number_max):
    guess = int(input('chose from {}-{}: '.format(number_min, number_max)))
    chances -= 1

# do guess
while (chances > 0) and (guess != secret):
    if guess < secret:
        guess = int(input('too small, guess again: '))
    elif guess > secret:
        guess = int(input('too big, guess again: '))
    chances -= 1
else:
    if guess == secret:
        print('NB')
    elif chances <= 0:
        print('Have no chance, Game Over！')
    else:
        print('Bug')
