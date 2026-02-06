class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    def get_info(self):
        return f"(self.name), age {self._age} years"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def get_info(self):
        return f"student : {super().get_info()}, ID: {self.student_id}"

class Teacher(Person):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject = subject
    def get_info(self):
        return f"Teacher: {super().get_info()}, Course: {self.subject}"

class Course:
    Course_count = 0
    def __init__(self,coursename):
        self.coursename = coursename
        self._students = []
        self._teachers = []
        Course.Course_count +=1
    def add_Student(self,student):
        self._students.append(student)
    def add_Teacher(self,teacher):
        self._teachers.append(teacher)
    def get_all(self):
        return {
            "Students":[s.get_info() for s in self._students],
            "Teachers":[t.get_info() for t in self._teachers],
        }
    @classmethod
    def total_courses(cls):
        return cls.Course_count
    @staticmethod
    def course_rules():
        return "Attendance should be greater than 90%."
    
Courseda = Course("Data Analyst")
CourseProgramming = Course("Programming")
s1 = Student ('Student1', 20, 'Stu101')
s2 = Student ('Student2', 22, 'Stu102')
t1 = Teacher ('Teacher1', 35, 'Computing')
CourseProgramming.add_Student(s1)
CourseProgramming.add_Student(s2)
CourseProgramming.add_Teacher(t1)
print(CourseProgramming.get_all())
print("Total number of courses", Course.total_courses())
print("Rule :::", Course.course_rules())
print (s1._name)