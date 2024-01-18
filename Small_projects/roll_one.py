# This program will roll a 6 sided die until exactly one of them roles a one

# Need to establish a counter
import random

i = 1
stop = 0
# now we create a while loop with an if and else
while stop < 1:
    if random.randrange(7) == 1 or random.randrange(7) == 1:
        stop += 1
    else:
        i += 1
print("It took", i, "rolls for exactly one dice to roll a 1")