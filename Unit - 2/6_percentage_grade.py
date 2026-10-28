# Calculate Grade from Percentage

percentage = float(input("Enter percentage: ")) 
if percentage >= 90: 
    grade = "A+" 
elif percentage >= 80: 
    grade = "A" 
elif percentage >= 70: 
    grade = "B" 
elif percentage >= 60: 
    grade = "C" 
elif percentage >= 50: 
    grade = "D" 
elif percentage >= 40: 
    grade = "E" 
else: 
    grade = "F" 
    
print("Percentage =", percentage) 
print("Grade =", grade)