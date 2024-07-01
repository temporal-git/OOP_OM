# инкапсуляция

class Person:
    def __init__(self, name, surname):
        self._name = name # _ нижнее подчеркивание показывает что атрибут приватный, к нему можно обратиться технически, но так делать не нужно
        self._surname = surname
        self.name = f'{self._name} {self._surname}'

p = Person("oleg", "mo")
print(p.name)