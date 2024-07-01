# ДИСКРИПТОРЫ

# ПРО УТЕЧКУ ПАМЯТИ (лучше пересмотреть ролик для пояснений)

import ctypes
def ref_count(obj_id):
    return ctypes.c_long.from_address(obj_id).value

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


v = Vector()
print(ref_count(id(v))) # получим 1 ссылку на обьект
id_v = id(v)

v.x = 5
print(ref_count(id(v))) # получим 2 ссылки на обьект

v.y = 5
print(ref_count(id(v))) # получим 3 ссылки на обьект

del v                   # удалим обьект, сборщик мусора удалит только 1 ссылку
print(ref_count(id_v))  # получим 2 ссылки на обьект

print(Vector.x._values)
print(list(Vector.x._values.keys())[0]) # утечка памяти, т.к. остались 2 ссылки после удаления объекта