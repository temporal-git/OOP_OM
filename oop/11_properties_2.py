# Способы задания геттеров и сетторов через property

class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print("From get_name()")
        return self._name

    def set_name(self, value):
        print("From set_name()")
        self._name =  value

    name = property()
    name = name.getter(get_name) # Вызываем метод геттер и передаем функцию get_name т.е. свойство name остается экземпляром класса проперти, но его метод получил аргумент
    name = name.setter(set_name)


p = Person("Dima")


print(p.__dict__)
print(p.name)
p.name = "Ivan"
print(p.__dict__)