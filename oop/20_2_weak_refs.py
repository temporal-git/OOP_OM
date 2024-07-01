# СЛАБЫЕ ССЫЛКИ

from weakref import WeakKeyDictionary


class IntDescriptor:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __set__(self, instance, value):
        self._values[instance] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance)


class Vector:
    x = IntDescriptor()
    y = IntDescriptor()


v = Vector()
print(hex(id(v)))

v.x = 10
print(Vector.x._values.keyrefs())

del v
print(Vector.x._values.keyrefs()) # получим пустой список