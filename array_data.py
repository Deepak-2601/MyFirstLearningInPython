from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 2, 5, 55, 65, 55, 10, 9, 7, 66, 11])

# arr2 = array('d', [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9])
# print(arr1)
# print(arr2)
# arr1.insert(2, 11)
# print(arr1)


# def traverse_array(array):
# for x in array:
# print(x)

# traverse_array(arr1)
# def access_element(array, index):
# if index >= len(array):
#   print("Sorry, the given element does not exist in the array!")
# else:
#   print(array[index])
# access_element(arr1, 10)
# def search_in_array(array, value):
# for i in array:
# if i == value:
# return array.index(value)
# return  "Sorry the number does not exist"


# print(search_in_array(arr1,int(input("Please enter a number: "))))
arr1.pop()
print(arr1)
print(arr1.index(8))
arr1.reverse()
print(arr1)
print(arr1.buffer_info())
arr1.append(10)
print(arr1.count(10))
print(arr1.tolist())
print(arr1[:])

