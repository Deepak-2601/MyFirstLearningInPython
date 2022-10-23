def fibonacci(n):
    if 0 <= n <= 1:
        return n
    n_number1, n_number2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_number2 + n_number1
        n_number2 = n_number1
        n_number1 = result

    return result


for i in range(369):
    print(i,fibonacci(i))
