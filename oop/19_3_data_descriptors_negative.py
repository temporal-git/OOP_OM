# ДИСКРИПТОРЫ
# пример почему плохо хранить данные в классе

from time import time
from time import sleep


class Epoch:
    def __get__(self, instance, owner_class):
        print(f"id of self: {id(self)}")
        if instance is None: # проверяем относится ли instance (что передается в качестве второго аргумента) к типу none.
            return self     # можно было записать и if not instance: тоже сработает, но нам неважно булевость, истинна она или ложна
        return int(time())

    def __set__(self, instance, value):
        pass


class MyTime:
    epoch = Epoch()


m = MyTime()
m1 = MyTime()

print(m.epoch) # Видим что id совпадает, т.е. два экземпляра класса mytime работают с одним и тем же объектом
sleep(1)
print(m1.epoch) # Что очень плохо. Для хранения данных нужны экземпляры классов (а не в классе)



