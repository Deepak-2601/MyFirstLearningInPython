def fun_print_fab(limit: int):
    v = 0
    v1 = 1
    for i in range(1, limit):
        f1 = v + v1
        v = v1
        v1 = f1
        print(f1)


def function_prime(prime: int):
    w = False
    for i in range(2, prime):
        if prime % 2 == 0:
            w = True
    if w == True:
        print("It is not a prime number")
    else:
        print("It is a prime number")


a = int(input("Please enter the number: "))
fun_print_fab(a)
b = int(input("Please enter the input: "))
function_prime(b)
