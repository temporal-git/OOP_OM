# ДИСКРИПТОРЫ
# Это атрибут объекта и этот атрибут сам является объектом определенного класса.
# Это тот класс у которого определены магические методы __get__() set или delete, или set name


from time import time


class Epoch:
    def __get__(self, instance, owner_class):
        print(f"Self: {self}")                  # Передал объект класса epoch, т.е. сам экземпляр дескриптора
        print(f"instance: {instance}")          # Получил обьект класса my time, это тот обьект, из которого произошло обращение к дескриптору
        print(f"owner_class: {owner_class}")    # Класс собственник это класс My time экземпляром которого является instance, второй аргумент
        return int(time())


class MyTime:
    epoch = Epoch()


m = MyTime()
print(m.epoch) # обращение через экземпляр
print(MyTime.epoch) # если обращение через класс, то instance ничего не получит и будет None


