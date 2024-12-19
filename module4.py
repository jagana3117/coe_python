# Write a python script to enter student number, name, marks in c, c++ and java calculate and display total marks, average, result and grade. Print fail if student average is less than 70.
no=int(input("Enter your number"))
name=input("Enter your name")
c=int(input("enter your marks in c"))
cpp=int(input("enter your marks in c++"))
java=int(input("enter your marks in c"))
total_marks=c+cpp+java
print("Total marks",total_marks)
average=total_marks/3
print("Result")
print("Average",average)
print("student number:",no)
print("Student name:",name)
print("Total marks:",total_marks)
print("Average:",average)
if(average>70):
    print("Pass")
else:
    print("Fail")