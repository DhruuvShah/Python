number = input("Enter a number: ")
digits = []

for digit in number:
    if digit.isdigit():
        digits.append(int(digit))

print(digits)