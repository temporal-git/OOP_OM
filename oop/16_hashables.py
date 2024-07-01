# хеширование
# клюем в словаре может быть только хэшируемый обьект

class Person:
    def __init__(self, name):
        self._name = name

    @property # делаем рид онли свойство (без сеттора) чтобы использовать в качестве объекта для хеширования
    def name(self):
        return self._name

    def __hash__(self): # переопределим метод хеш
        return hash(self.name)

    def __eq__(self, person_obj): # переопределим метод равенства
        return isinstance(person_obj, Person) and self.name == person_obj.name


p1 = Person("Ivan") # заведем двух Иванов и сравним
p2 = Person("Ivan")
print(p1 == p2)

p3 = Person("Oleg")
print(p1 == p3) # не равны

print(hash(p1)) # хеш у равных значений одинаковый
print(hash(p2))

d = {p1: "Ivanov Ivan"} # можно использовать в качестве ключа словаря
print(d.get(p1))