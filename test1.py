a = []
b = ""
i = 0
y = False
while i < 5:
    b = input(f"Please enter {i} name to the list: ")
    a.append(b)
    i = i + 1
c = input("Please enter the name to check: ")
j = 0
while j < len(a):
    if c == a[j]:
        y = True
    j = j + 1

if y == True:
    print("The name exist in the given list")
else:
    print("Sorry, the name does not exist in the given list")
