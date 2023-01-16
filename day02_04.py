
# import random
# secret = int(random.randint(1, 10))
# guess = int(random.randint(1, 10))
#
# #secret = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #guess = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# if guess < secret:
#     print('too low')
# elif guess == secret:
#     print('just right')
# else:
#     print('too high')

secret = random.randint(1, 10)
guess = int(input(‘정답은?’)
If secret == guess:
    Print(“정답입니다!”)
Elif guess > secret:
    Print(f”정답보다 큰 수 입니다. 정답은 {secret}”)
Else:
    Print(f”정답보다 작은 수 입니다. 정답은 {secret}”)
