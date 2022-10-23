def lowest_number(a: list):
    value = a[0]
    l1 = len(a)
    for i in range(1, l1):
        if a[i] < value:
            value = a[i]
    return value


def highest_number(a: list):
    value = a[0]
    l1 = len(a)
    for i in range(1, l1):
        if a[i] > value:
            value = a[i]
    return value


if __name__ == "__main__":
    b = [77, 22, 90, 75, 12, 33, 45, 67, 56, 55, 987, 999, 678, 0]
    v1 = lowest_number(b)
    print(v1, "is the lowest number")
    v2=highest_number(b)
    print(v2,"is the highest number")
    c = [164739, 25674, 65632, 209470, 34562837, 674539]
    v1 = lowest_number(c)
    print(v1, "is the lowest number")
    v2 = highest_number(c)
    print(v2, "is the highest number")
    d = [32123, 433133, 98877484, 634274734, 9876677784, 213445]
    v1 = lowest_number(d)
    print(v1, "is the lowest number")
    v2 = highest_number(d)
    print(v2, "is the highest number")