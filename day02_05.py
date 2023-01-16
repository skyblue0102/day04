
# import random
# small = bool(random.randint(0,1))
# green = bool(random.randint(0,1))
# if small:
#     if green:
#         print('pea')
#     else:
#         print('cherry')
# else:
#     if green:
#         print('watermelon')
#     else:
#         print('pumpkin')

import random
small = random.choice([True, False])
print(small)
green = random.choice([True, False])
print(green)

if small:
    if green:
        print('완두콩 입니다')
    else:
        print('체리 입니다')
else:
    if green:
        print('수박 입니다')
    else:
        print('호박 입니다')


