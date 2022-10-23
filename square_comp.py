number = [1, 2, 3, 4, 5, 6]
n1 = int(input("please enter the number: "))
square = [n1 **2 for n1 in number]
index_pos = number.index(n1)
print(square[index_pos])

