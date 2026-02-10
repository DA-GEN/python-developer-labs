class Student:
    """
    A class to represent a student with their name, age, and grades."""
    
    def __init__(self, name: str, age: int, grades: dict[str, int]):
        self.name = name
        self.age = age
        self.grades = grades


    def add_grade(self, subject: str, grade: int):
        self.grades[subject] = grade


    def average_grade(self) -> float:
        if not self.grades:
            return 0.0

        total = sum(self.grades.values())
        return total / len(self.grades)


class StudentGroup:
    """
    A class to manage a group of students.
    """

    def __init__(self):
        self.students = []


    def add_student(self, student: Student):
        self.students.append(student)


    def get_best_student(self) -> Student:
        if not self.students:
            return None
        
        best_student = self.students[0]
        for student in self.students[1:]:
            if student.average_grade() > best_student.average_grade():
                best_student = student
        
        return best_student



