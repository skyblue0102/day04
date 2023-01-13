
import random
small = bool(random.randint(0,1))
green = bool(random.randint(0,1))
if small:
    if green:
        print('pea')
    else:
        print('cherry')
else:
    if green:
        print('watermelon')
    else:
        print('pumpkin')