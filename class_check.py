class check:
    def __init__(self):
        print("Inside class int")
    def check_highest(self, a: list):
        z = a[0]
        for i in range(1, len(a)):
            if a[i] > z:
                z = a[i]
        return z

    def check_lowest(self, a: list):
        x = a[0]
        for i in range(1, len(a)):
            if a[i] < x:
                x = a[i]
        return x


v1 = check()

u = [7, 5, 10, 1, 70, 85, 97, 19, 11, 20, 8, 10]
l = v1.check_highest(u)
print(l)
l1 = v1.check_lowest(u)
print(l1)