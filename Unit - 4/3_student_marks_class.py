"""  Write a Python program to create a student class (id, Name, mid1_marks, mid2_marks,  
quiz_marks). Create a student objects and write a function marksList() to display student’s  
result as given below:  
ROLL NUMBER:  
NAME:  
MID1:  
MID2:  
QUIZ:  
TOTAL: MID1+MID2+QUIZ  
RESULT: A GRADE (IF TOTAL>=80), B GRADE (TOTAL<80 and TOTAL>=60), C  
GRADE (TOTAL>=50 and TOTAL<60) """

class Student:
    def __init__(self, student_id, name, mid1, mid2, quiz):
        self.student_id = student_id
        self.name = name
        self.mid1 = mid1
        self.mid2 = mid2
        self.quiz = quiz

    def markList(self):
        total = self.mid1 + self.mid2 + self.quiz

        if total >= 80:
            grade = "A Grade"
        elif total >= 60:
            grade = "B Grade"
        elif total >= 50:
            grade = "C Grade"
        else:
            grade = "No grade specified"

        print("\n--- Mark Sheet ---")
        print("Roll Number:", self.student_id)
        print("Name:", self.name)
        print("Mid1:", self.mid1)
        print("Mid2:", self.mid2)
        print("Quiz:", self.quiz)
        print("Total:", total)
        print("Result:", grade)

sid = input("Enter roll number: ")
name = input("Enter name: ")
mid1 = float(input("Enter mid1 marks: "))
mid2 = float(input("Enter mid2 marks: "))
quiz = float(input("Enter quiz marks: "))

student = Student(sid, name, mid1, mid2, quiz)
student.markList()
