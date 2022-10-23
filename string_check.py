a = ["India", "U.S.A", "Russia", "Germany", "Denmark", "Japan"]
b = "India"
for c in range(0, len(a)):
    if b == a[c]:
        x = True
if x == True:
    print("It exist")
else:
    print("It does not exist")