def is_palindrome(string):
    backwards = string[::-1]
    return backwards.casefold() == string.casefold()


word = input("Please enter the sentence: ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
