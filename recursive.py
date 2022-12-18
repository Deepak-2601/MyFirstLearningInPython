def factorial(n):
    assert 0 <= n == int(n), 'The given number must be positive and whole integer only[eg:2,3,7,10]'
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(0))
