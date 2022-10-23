import random


def get_integer(prmote):
    while True:
        temp = input(prmote)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{0} is not the valid format".format(temp))


highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing
guess = 0
print(" Please guess the number between 1 and {}: ".format(highest))

while guess!= answer:
    guess = get_integer(":")
    if guess==0:
        break
    else:
        if guess<answer:


