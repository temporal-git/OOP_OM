# Способы задания геттеров и сетторов через property

"""
Функция property() используется для определения свойств в классах.
Метод property() обеспечивает интерфейс для атрибутов экземпляра класса. Он инкапсулирует атрибуты экземпляров и предоставляет свойства, аналогично тому, как это работает в Java и C#.
Метод property() принимает на вход методы get, set и delete, и возвращает объекты класса property.
Вместо метода property() лучше использовать декоратор property
"""


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print("From get_name()")
        return self._name

    def set_name(self, value):
        print("From set_name()")
        self._name =  value

    name = property(fget=get_name, fset=set_name) # внутри нашего класса Person создадим переменную name которая будет экземпляром класса Property
    # и переменная name становится свойством, атрибутом класса
    # класс Property имеет два параметра fget= чтение свойства и fset= устанавливает приватное свойство.
    # Name станвоистя свойством класса и его не будет в пространстве имен.


p = Person("Dima")


print(p.__dict__)
print(p.name)
p.name = "Ivan"
print(p.__dict__)