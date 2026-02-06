class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_info(self):
        return F"{self.name} is {self.age} years old."
class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id
    def get_student(self):
        print(f"ID of Student is {self.student_id}")

p1 = Person('Aaron',30)
Stu1 = Student('Jeremy',25,'St110')
print(p1.get_info())
Stu1.get_info()
Stu1.get_student()