
import random
secret = int(random.randint(1, 10))
guess = int(random.randint(1, 10))

#secret = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#guess = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if guess < secret:
    print('too low')
elif guess == secret:
    print('just right')
else:
    print('too high')