def decimal_to_binary(w):
    assert int(w) == w, 'Sorry,the given parameter should be an integer only example: [2,4,10,23,67,88]'
    if w == 0:
        return 0
    else:
        return w % 2 + 10 * decimal_to_binary(int(w / 2))


print(decimal_to_binary(1.3))