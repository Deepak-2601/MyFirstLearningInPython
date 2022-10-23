numbers = set()
numbers.add(1)
print(numbers)
while len(numbers) < 5:
    next_number = int(input("Please enter the number: "))
    numbers.add(next_number)
print(numbers)
