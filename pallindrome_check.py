def is_palindrome(word):
    back = word[::-1]
    if back.casefold() == word.casefold():
        return "It is a palindrome"
    else:
        return "It is not a palindrome"


v1 = input("Please enter the word to check ")
a = is_palindrome(v1)
print(a)

