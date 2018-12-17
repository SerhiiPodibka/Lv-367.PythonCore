import random
def makeMove(sticks):
    if sticks%4 == 0:
        return random.randint(1, 3) 
    return sticks%4
