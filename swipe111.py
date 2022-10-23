a = [1, 2, 3, 4, 5]
l = len(a)
x = a[l - 1]
for i in range(1, l):
    a[l - i] = a[l - (i + 1)]
a[0] = x
print(a)
