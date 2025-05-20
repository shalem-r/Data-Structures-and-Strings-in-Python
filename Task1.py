#Student Dictionary

student_marks ={"Alice" : 85,
               "Rohit" : 65,
               "Virat" : 95}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student Not found.")