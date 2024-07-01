class Person:
    name = "Ivan"

    def hello():
        print("Hello")


p1 = Person()
p2 = Person()

print(p1)
print(id(p1))  # разные объекты
print(p2)
print(id(p2))  # разные объекты

print(p1.name)
print(p2.name)

print(id(p1.name))  # одно и то же свойство
print(id(p2.name))  # одно и то же свойство

print(
    p1.__dict__)  # Пространство имен т.е. локальный словарь для объектов p1 и p2 пустой, поэтому будет искать дальше в слвоаре класса
print(p2.__dict__)

p1.name = "oleg"
p2.name = "dima"

print(p1.__dict__)  # в локальных словарях появились значения для атрибута name и они разные
print(p2.__dict__)

p2.age = 123  # динамически добавим новое свойство (атрибут) для объекта p2, но для p1 оно не появится, так же как и для класса Person

print(p2.__dict__)

print(p1.name)
print(p2.name)

print(Person.__dict__)

p1 = Person()  # переопределяем p1 и p2
p2 = Person()

Person.name = "fsfsfsf"

print(p1.name)
print(p2.name)
