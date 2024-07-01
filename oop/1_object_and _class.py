class Person:
    name = "Ivan"


print(Person.name)  # покажет значения свойства класса name
print(Person.__name__)  # покажет имя класса
print(dir(Person))  # покажет атрибуты класса

print(Person.__class__)  # покажет тип класса

p = Person()  # Создаем объект или экземпляр класса. Вызов объекта возвращает его объект
print(p)
print(p.__class__)  # возвращает тип объекта
print(p.__class__.__name__)
print(
    type(p))  # возвращает тип объекта как и метод __class__, возвращает именно класс как объект, который можно вызвать

new_person = type(p)()  # создав новый экземпляр того же типа, что и объект P
print(new_person)
