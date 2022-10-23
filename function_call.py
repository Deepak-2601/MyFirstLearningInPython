def is_prime(num):
    for n in range(2, num):
        if (num % n == 0):
            return str(num) + " is not a prime"
        else:
            return str(num) + " is a prime"


a = [11, 15, 10, 9, 8, 7, 12, 17, 29, 99, 39, 41, 73, 71, 75, 90, 91, 23,554,32,67,77,765,651,45,435,6,9,654]
for i in range(0, len(a)):
    x = is_prime(a[i])
    print(x)
