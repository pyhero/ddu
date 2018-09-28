import string

digits = string.digits
letters = string.ascii_letters
special = '~!@#$%^&*()_=-/,.?<>;:[]{}|\)'

secret = input('Input your password: ')

digits_switch, letters_switch, special_switch, bad_switch = 0, 0, 0, 0
for l in secret:
    if l in digits:
        digits_switch = 1
    elif l in letters:
        letters_switch = 1
    elif l in special:
        special_switch = 1
    else:
        bad_switch = 1
        print('Bad Password, can not contain {}'.format(l))
        break

if bad_switch == 0:
    print('Password invalid!')
else:
    if len(secret) <= 8 or secret.isdigit() or secret.isalpha():
        print('Low')
    elif len(secret) > 8 and digits_switch + letters_switch + special_switch == 2:
        print('Mid')
    elif len(secret) > 16 and digits_switch + letters_switch + special_switch == 3 and secret.startswith(letters):
        print('High')
    else:
        print('Not limited.')
