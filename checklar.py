def check_largest_number(x: list):
    y = x[0]

    for i in range(1, len(x)):
        if x[i] > y:
            y = x[i]
    return y


a = [1, 7, 67, 45, 32, 12, 34, 90, 784, 76, 55]
l1 = check_largest_number(a)
print(l1)
