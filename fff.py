def average(*args):
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


print(average(122345665445,12342344456, 29087688, 35445566432, 4212323, 543443))
