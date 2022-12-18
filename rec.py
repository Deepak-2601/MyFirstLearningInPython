def fibonacci(n):
    assert 0 <= n == int(n),"Sorry the given number should be a positive and whole integer example: [2,9,10,7]"
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(8))
