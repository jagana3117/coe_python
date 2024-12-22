def calculate_average(marks):
    return sum(marks) / len(marks)
def top_performer(students):
    averages = {name: calculate_average(marks) for name, marks in students.items()}
    return max(averages, key=averages.get)
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
average_marks = {name: calculate_average(marks) for name, marks in students.items()}
top_student = top_performer(students)
print(f"Average Marks: {average_marks}")
print(f"Top Performer: {top_student}")
