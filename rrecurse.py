word =input("enter a word")
# word = "madam"
def is_palindrome_1(word):
    return word == word[::-1]
print("** is_palindrome_1 **", is_palindrome_1(word))

