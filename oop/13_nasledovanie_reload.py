

class Person:
    def hello(self):
        print("Im Person")

class Student(Person):
    def hello(self):
        print("Im Student")

    def goodbye(self):
        print("Goodbye")

s = Student()


s.hello() # использует метод описанный в дочернем классе student, а не родительском
print(s.__dict__)
print(Student.__dict__)