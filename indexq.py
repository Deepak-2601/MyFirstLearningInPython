a = [15, 98, 78, 0, 5, 32, 11, 54, 34]
x = int(input("Please enter the number to check: "))
z=False
i=0
for i in range(0, len(a)):
    if x == a[i]:
       z=True
if z==True:
    print(x, f"exist in index {i}")
else:
    print(f"Sorry {x} does not exist")

