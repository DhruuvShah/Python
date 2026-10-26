def is_palindrome(number):
    original = str(number)
    return original == original[::-1]

n = input("Enter a number: ")

if is_palindrome(n):
    print("Palindrome number")
else:
    print("Not a palindrome number")