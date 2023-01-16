#6.2

guess_me = 7
number = 1
while True:
    if number < guess_me:
        print('too low')
    if number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
number = number + 1