import student_manager

if __name__ == "__main__":
    student1 = student_manager.Student("Alice", 20, {"Math": 85, "English": 90})
    student2 = student_manager.Student("Bob", 22, {"Math": 78, "English": 88})
    student3 = student_manager.Student("Charlie", 21, {"Math": 92, "English": 95})

    teacher1 = student_manager.Teacher("Carl", 40, "Math")

    group = student_manager.StudentGroup(teacher1)
    group.add_student(student1)
    group.add_student(student2)
    group.add_student(student3)

    best_student = group.get_best_student()
    if best_student:
        print(f"\nThe best student is {best_student.name} with an average grade of {best_student.average_grade():.2f}.\n")
    else:
        print("\nNo students in the group.\n")
    
    print(group.describe_group())