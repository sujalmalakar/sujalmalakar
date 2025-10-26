class students:
    def __init__(self, name, class_roll):
        self.name = name
        self.class_roll = class_roll
    def attendance(self, times):
        for i in range(times):
            print(f"{self.name} is present.")

class Teacher:
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} is present.")
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"{student.name} is absent.")
    def greet_students(self):
        for student in self.students:
            print(f"{student.name}, Student says: Moi")

student1 = students( "Falcon", class_roll=5)
student2 = students("LOCO", class_roll=8)
student3 = students("Pikopik", class_roll=4)
student4 = students("Hang", class_roll=3)
student5 = students("Kiyo", class_roll=7)
teacher = Teacher()
teacher.add_student(student1)
teacher.add_student(student2)
teacher.add_student(student3)
teacher.greet_students()
teacher.add_student(student4)
teacher.add_student(student5)
teacher.greet_students()