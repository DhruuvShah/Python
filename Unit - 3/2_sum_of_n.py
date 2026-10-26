n= int(input("Enter a number: "))
total = 0.0

for i in range(8, n + 1):
    total += 1 / i

print("Sum of series:", total)
