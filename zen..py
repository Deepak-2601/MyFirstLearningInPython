x = [10, 2, 39, 67, 76, 55, 31, 75, 22, 112, 9000]
y = 7
a=False
for i in range(0, len(x)):
    if y == x[i]:
        a = True
        break
if a == True:
    print("The given number exist")
else:
    print("The given number does not exist")
