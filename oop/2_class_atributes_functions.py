class Person:
    name = "Ivan"
    def hello():
        print("Hello")

print(Person.__dict__) # магический метод __дикт__ покажет пространство имен класса

# Person.__dict__["name"] = "sdfsfg" #так нельзя присвоить свойство через словарь, для этого есть специальные функкции вида setattr

Person.age = 23424 # добавит новое свойство класса через дот-натацию .age
print(Person.__dict__)

print(getattr(Person, "name")) # getattr позволяет получить значение атрибута класса

setattr(Person, "birthdate", "123") # setattr позволяет добавить атрибут или изменить значение атрибута класса
print(Person.__dict__)

delattr(Person, "birthdate") # удаляет атрибут
print(Person.__dict__)

# Person.hello() # вызов функции класса
