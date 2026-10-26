# List Methods

numbers = [10, 20, 30, 40] 
print("Original list:", numbers) 

numbers.insert(2, 25) 
print("After insert():", numbers) 

numbers.remove(25) 
print("After remove():", numbers) 

numbers.append(50) 
print("After append():", numbers) 
print("Length using len():", len(numbers)) 

removed = numbers.pop() 
print("Popped item:", removed) 
print("After pop():", numbers) 

numbers.clear() 
print("After clear():", numbers) 

numbers = [10, 20, 30] 
del numbers[1] 
print("After del:", numbers) 