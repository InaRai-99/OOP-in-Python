class Person:
    def __init__(self,name):
        self.name =name
        print("Constructor Called")

    def hi(self):
        print("Hi, Method of class person")
    def hello(self):
        print(f"Hello {self.name}")

p1 = Person('Roman')
p2 =Person('Ron')
p1.hi()
p1.hello()
p2.hello()