# Способы задания геттеров и сетторов через property

class Person:
    def __init__(self, name):
        self._name = name

    @property # заменяем оригинальную функцию на экземпляр класса проперти с тем же именем, что и оригинальная функция, но при помощи декоратора
    def name(self):
        return self._name

    # name = property(name) # переопределяем name

    @name.setter
    def name(self, value):
        self._name = value

    # name = name.setter(set_name) # переопределяем name


p = Person("Dima")


print(p.__dict__)
print(p.name)
p.name = "Ivan"
print(p.__dict__)