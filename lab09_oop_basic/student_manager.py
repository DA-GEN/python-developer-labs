from typing import Optional


class Student:
    """
    A class to represent a student with their name, age, and grades."""
    
    def __init__(self, name: str, age: int, grades: dict[str, int]):
        self.name = name
        self.age = age
        self.grades = grades if grades is not None else {}

    def add_grade(self, subject: str, grade: int):
        self.grades[subject] = grade


    def average_grade(self) -> float:
        if not self.grades:
            return 0.0

        total = sum(self.grades.values())
        return total / len(self.grades)
    
        
    def __repr__(self) -> str:
        """Позволяет красиво печатать объект Student."""
        return f"Student(name='{self.name}', avg={self.average_grade():.2f})"


class StudentGroup:
    """
    A class to manage a group of students.
    """

    def __init__(self):
        self.students = []


    def add_student(self, student: Student):
        self.students.append(student)


    def get_best_student(self) -> Optional[Student]:
        if not self.students:
            return None
        
        return max(self.students, key=lambda s: s.average_grade())


    def __iter__(self):
        """
        Makes the group iterable: can be used in a loop for students in the group.
        """
        return iter(self.students)


