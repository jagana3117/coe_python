class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = int(student_id)
        self.student_name = student_name
        self.student_class = student_class
    def display(self):
        print("Student Id:",self.student_id)
        print("Student Name:",self.student_name)
        print("Student Class:",self.student_class)
student_id=input("enter student id: ")
student_name=input("enter student name: ")
student_class=input("enter student class: ")
stu=Student(student_id,student_name,student_class)
stu.display()

