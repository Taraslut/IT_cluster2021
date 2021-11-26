# import random
from random import randint, choice
from my_modules.sub_pac1.helper1 import multipy as m # absolute


days = ['Monday', "Thursday", 'Wednesday', "Thursday", "Friday", "Saturday", 'Sunday']

# rand_number = random.randint(1, 10)
rand_number = randint(1, 10)
print(rand_number)

rand_day = choice(days)
print(rand_day)
