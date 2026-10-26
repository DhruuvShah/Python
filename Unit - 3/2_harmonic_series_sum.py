"""Calculate the sum of the reciprocal series from 1/8 through 1/N."""

n= int(input("Enter a number: "))
total = 0.0

for i in range(8, n + 1):
    total += 1 / i

print("Sum of series:", total)
