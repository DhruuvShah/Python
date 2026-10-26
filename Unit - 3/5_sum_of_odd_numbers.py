"""Find the sum of all odd numbers from 1 to N using a function."""

def sum_odd(n):
    total = 0
    for number in range(1, n + 1, 2):
        total += number
    return total

n = int(input("Enter a number: "))
print("Sum of odd number:", sum_odd(n))
