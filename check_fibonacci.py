n1 = 0
n2 = 1
for i in range(1,11):
    f1 = n1 + n2
    n1 = n2
    n2 = f1
    print(f1)