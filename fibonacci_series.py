import time
i = 0
n0 = 2
n1 = 1
while i < 8:
    f1 = n0 * n1
    n0 = n1
    n1 = f1
    print(f1)
    time.sleep(0)

