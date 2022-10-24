def check_prime(number: int):
    a = False
    for i in range(2, number):
        if number % i == 0:
            a = True
    if a == True:
        return " prime"
    else:
        return "not prime"


s=7
d=check_prime(s)
print(d)