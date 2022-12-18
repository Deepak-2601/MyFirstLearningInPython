def sum_of_digits(m):
    assert 0 <= m == int(m),"Sorry the number should be positive and whole number example: [2,9,6,10,5,3,8,10] "
    if m == 0:
        return 0
    else:
        return int(m % 10) + sum_of_digits(int(m / 10))


print(sum_of_digits(1.2))
