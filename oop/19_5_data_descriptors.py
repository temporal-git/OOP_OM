# ДИСКРИПТОРЫ

class IntDescriptor:
    def __init__(self):
        self._values = {} # заведем словарь для хранения значений

    def __set__(self, instance, value):
        self._values[instance] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance)
class Vector:
    x = IntDescriptor()
    y = IntDescriptor()

v1 = Vector()
v2 = Vector()

v1.x = 5
print(v2.x)
v2.x = 10
print(v1.x)
print(v2.x)
print(v1.__dict__)
print(Vector.x._values) # словарь с ключами в виде объектов