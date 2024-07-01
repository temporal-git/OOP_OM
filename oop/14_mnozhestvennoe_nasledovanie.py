# print(s.__class__.mro()) # выведет порядок наследования

class Person:
    def hello(self):
        print("Im Person")

class Student(Person):
    def hello(self):
        print("Im Student")

class Prof(Person):
    def hello(self):
        print("Im Prof")

class Someone(Student, Prof): # Класс имеет сразу два родителя. Какойб чей метод он будет использовать при вызове?
    pass

s = Someone()

s.hello() # В
# Выдаст Im Student из-за правил mro() method resolution order.
# Кто левее тот и прав, порядок имеет значение при создании класса.
print(s.__class__.mro()) # выведет порядок наследования