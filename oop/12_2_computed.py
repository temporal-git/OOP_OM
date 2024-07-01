# Read only свойства, задаются как обычные через property, но прописывается только getter. Без setter


class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    @property
    def full_name(self):
        return f'{self._name} {self._surname}'


p = Person("Ivan", "Ivanoff")
print(p.full_name) # выводим вычисляемое свойство, оно вычисляется каждый раз при обращении

p.surname = "Petroff"
print(p.full_name)