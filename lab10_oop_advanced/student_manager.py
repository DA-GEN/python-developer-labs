from typing import Optional


class Person:
    """
    A base class to represent a person with a name and age.
    """
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Student(Person):
    """
    A class to represent a student with their name, age, and grades.
    """
    
    def __init__(self, name: str, age: int, grades: dict[str, int]):
        super().__init__(name, age)
        self.grades = grades if grades is not None else {}


    def add_grade(self, subject: str, grade: int) -> None:
        self.grades[subject] = grade


    def average_grade(self) -> float:
        if not self.grades:
            return 0.0


        total = sum(self.grades.values())
        return total / len(self.grades)
    

    def get_grades(self) -> list[int]:
        return list(self.grades.values())


    def __repr__(self) -> str:
        """
        Allows you to print the Student object beautifully.
        """
        return f"Student(name='{self.name}', avg={self.average_grade():.2f})"


class Teacher(Person):
    """
    A class to represent a teacher with their name, age, and subject they teach.
    """

    def __init__(self, name: str, age: int, subject: Optional[str]):
        super().__init__(name, age)
        self.subject = subject if subject is not None else None


class StudentGroup:
    """
    A class to manage a group of students.
    """

    def __init__(self, teacher: Teacher):
        self.students = []
        self.teacher = teacher
    

    def add_student(self, student: Student):
        self.students.append(student)


    def get_best_student(self) -> Optional[Student]:
        if not self.students:
            return None
        
        return max(self.students, key=lambda s: s.average_grade())
    

    def get_mid_grade(self) -> Optional[float]:
        if not self.students:
            return None
        
        total_sum = sum(sum(s.get_grades()) for s in self.students)
        total_len = sum(len(s.get_grades()) for s in self.students)
        return total_sum / total_len if total_len > 0 else None
    

    def describe_group(self) -> str:
        if not self.students:
            return f"Group under {self.teacher.name} is empty."
        
        names = ', '.join(s.name for s in self.students)
        
        avg = self.get_mid_grade()
        avg_str = f"{avg:.2f}" if avg is not None else "N/A"
        
        return (f"Teacher's name: {self.teacher.name}\n"
                f"List of students: {names}\n"
                f"Mid grade: {avg_str}")

    
    def __iter__(self):
        """
        Makes the group iterable: can be used in a loop for students in the group.
        """
        return iter(self.students)


