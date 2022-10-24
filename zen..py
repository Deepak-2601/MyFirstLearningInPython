def fab_fun(a: int):
    x = 0
    y = 1
    for i in range(1, a):
        l = x + y
        x = y
        y = l
        print(l)


v = int(input("Please enter the number: "))
fab_fun(v)

