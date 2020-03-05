import random


def randomID():
    with open("RAW1", 'r') as file:
        line = file.read()
        line = line.split(' ')
        n = random.randint(50, 200)
        el = random.choice(line)
        print(el)


randomID()