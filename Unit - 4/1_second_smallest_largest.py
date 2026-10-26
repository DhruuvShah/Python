"""Find the second smallest and second largest distinct values in a list."""

numbers = list(map(int,input("Enter number separated by space: ").split()))
temp_numbers = sorted(set(numbers))

if len(temp_numbers) < 2:
    print("At least 2 distinct values are required.")
else:
    print("Second smallest:", temp_numbers[1])
    print("Seond largest:", temp_numbers[-2])
