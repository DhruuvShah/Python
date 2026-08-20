print("----- MENU -----") 
print("1. Area of Circle") 
print("2. Area of Triangle") 
print("3. Area of Square") 
print("4. Area of Rectangle") 
print("5. Simple Interest") 

choice = int(input("Enter your choice: ")) 

if choice == 1: 
	r = float(input("Enter radius: ")) 
	print("Area of Circle =", 3.14 * r * r) 
elif choice == 2: 
	b = float(input("Enter base: ")) 
	h = float(input("Enter height: ")) 
	print("Area of Triangle =", 0.5 * b * h) 
elif choice == 3: 
	side = float(input("Enter side: ")) 
	print("Area of Square =", side * side) 
elif choice == 4: 
	length = float(input("Enter length: ")) 
	breadth = float(input("Enter breadth: ")) 
	print("Area of Rectangle =", length * breadth) 
elif choice == 5: 
	p = float(input("Enter principal: ")) 
	r = float(input("Enter rate: ")) 
	t = float(input("Enter time: ")) 
	print("Simple Interest =", (p * r * t) / 100) 
else: 
	print("Invalid choice")