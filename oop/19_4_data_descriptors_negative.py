# ДИСКРИПТОРЫ
# пример почему плохо хранить данные в дескрипторе

from time import time

# пример плохого использования и хранения данных в дескрипторе


class IntDescriptor:
    def __set__(self, instance, value):
        self._value = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._value


class Vector:
    x = IntDescriptor()
    y = IntDescriptor()


v = Vector()
v.x = 5

v2 = Vector()
print(v.x)
v2.x = 200
print(v.x) # получаем что изменя x для v2  у нас меняется и v

