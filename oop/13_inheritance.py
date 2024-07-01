
class Person:
    age = 0
    def hello(self):
        print("Hello")

class Student(Person):
    pass

s = Student()

print(dir(s)) # экземпляру класса student доступны свойство age и метод hello
# хотя в классе студент они не описаны
print(s.age)
s.hello()

print(s.__dict__) # словарь пустой

print(Person.__dict__) # методы и свойства определены в родительском классе