# Read only свойства, задаются как оыбчные через property, но прописывается только getter. Без setter


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


p = Person("Dima")

print(p.name)

# p.name = "Ivan" # при попытке изменить значение, выдаст ошибку (исключение) т.к. свойство только для чтения