# Dictionary Methods 

student = { 
"name": "Rahul", 
"age": 22, 
"course": "MCA" 
} 

print("Dictionary:", student) 
print("Items:", student.items()) 
print("Name:", student["name"]) 
print("Course:", student.get("course")) 
student["age"] = 23 
print("After changing age:", student) 
print("Length:", len(student)) 