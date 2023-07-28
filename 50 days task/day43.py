def student_marks():
    marks_dict = {}

    while True:
        name = input("Enter student name (or 'done' to finish): ")
        if name == "done":
            break

        marks = float(input("Enter marks achieved by the student: "))
        marks_dict[name] = marks

    return marks_dict

# Test the function
result = student_marks()
print(result)
