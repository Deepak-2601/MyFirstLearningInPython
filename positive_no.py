def positive_number(b: list):
    for i in range(0, len(b)):
        if b[i] > 0:
            print(b[i])


def negative_number(a: list):
    for i in range(0, len(a)):
        if a[i] < 0:
            print(a[i])


def create_list(no_of_element: int) -> list:
    a = []
    for i in range(no_of_element):
        b = int(input("Please enter the {i} number to the list: "))
        a.append(b)

    print("inside function list:", a)
    return a


l1 = create_list(3)
positive_number(l1)
negative_number(l1)
l2=create_list(5)
positive_number(l2)