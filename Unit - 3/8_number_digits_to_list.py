"""Create a list whose elements are the digits of an entered number."""

number = input("Enter a number: ")
digits = []

for digit in number:
    if digit.isdigit():
        digits.append(int(digit))

print(digits)
