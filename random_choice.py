
# 
# Requirements:
# •	The program must include a function named print_random that takes three arguments: a, b, c.
# •	In the print_random function, the random module should be used to randomly select one of the arguments passed.
# •	The print_random function should print a randomly chosen argument from a, b, c each time it's called.
# 


import random


def print_random(a, b, c):
    rand_selection = random.choice([a,b,c])
    print(rand_selection)


print_random("obi", "atiku", "BAT")