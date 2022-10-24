primecount=0
for y in range(1, 100):
    x = y
    a=""
    for i in range(2, x):
        if x % i== 0:
            a = "not prime"
    if a == "not prime":
        pass
    elif primecount < 10 :
        primecount=primecount +1
        print(x)


