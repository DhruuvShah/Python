text = input("Enter a string: ")
target = input("Enter the character to count: ")
count = 0

for character in text:
    if character == target:
        count += 1

print("Occurrence:", count)