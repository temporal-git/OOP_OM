# Read only свойства, задаются как обычные через property, но прописывается только getter. Без setter


class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._full_name = None # добавили новое свойство

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._full_name = None # добавили новое свойство

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value
        self._full_name = None # добавили новое свойство

    @property
    def full_name(self):
        if self._full_name is None: # Делаем проверку является ли приватное свойство _full_name равным None или нет. Если содержит значение отличное от None, то возвращаем его
            self._full_name = f'{self._name} {self._surname}'
        return self._full_name


p = Person("Ivan", "Ivanoff")

print(p.__dict__)
print(p.full_name) # выводим вычисляемое свойство, оно вычисляется каждый раз при обращении
print(p.__dict__) # в словаре видим что результат закешировался

p.surname = "Petroff"
print(p.__dict__) # видим что результат сбросился
print(p.full_name) # вычисляем заново фул нейм
print(p.__dict__) # результат опять закешировался