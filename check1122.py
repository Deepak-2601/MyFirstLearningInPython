a = [123434322,43442442,53553244,6732255673,334323455]
x = a[0]
for i in range(0, len(a)):
    if a[i] > x:
        x = a[i]
y=a[0]
for s in range(0,len(a)):
    if a[s] > y and y < x:
        y = a[s]
        print(y,"Is the second largest number")