# student_marks.py

def get_student_marks():
    student_marks = {
        "Alice": 85,
        "Bob": 90,
        "Charlie": 78,
        "David": 92,
        "Eva": 88
    }

    name = input("Enter student name: ")

    if name in student_marks:
        print(f"{name}'s marks: {student_marks[name]}")
    else:
        print(f"Student '{name}' not found in the record.")

if __name__ == "__main__":
    get_student_marks()
