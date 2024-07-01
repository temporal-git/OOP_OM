# ДИСКРИПТОРЫ
# Это атрибут объекта и этот атрибут сам является объектом определенного класса.
# Это тот класс у которого определены магические методы __get__() set или delete,
# или set name


# class Person:
#     def __init__(self, name, surname):
#         self._name = name # свойства name и surname должны быть всегда строками, чтобы мы им не могли что-то другое, не строковое значение
#         self._surname = surname
#         self._full_name = None
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value
#         self._full_name = None
#
#     @property
#     def surname(self):
#         return self._surname
#
#     @surname.setter
#     def surname(self, value):
#         self._surname = value
#         self._full_name = None


# использование дескриптора:

# class StringD:
#     def __init__(self, value):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self._value = value
#
#     def get(self):
#         return self._value
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = StringD(name)
#         self.surname = StringD(surname)
#
#
# p = Person("Ivan", "Ivanov")
#
# print(p.name.get())


from time import time
from random import choice

class Epoch:
    def __get__(self, instance, owner_class):
        return int(time())
class MyTime:
    epoch = Epoch()

# m = MyTime()
# print(m.epoch)

# КОД ДЛЯ ОДНОЙ ИГРЫ В БРОСОК ИГРАЛЬНОГО КУБИКА
class Dice:
    @property
    def number(self):
        return choice(range(1, 7))
# d = Dice()
# print(d.number)


# КОД  ДЛЯ ТРЕХ ИГР: КУБИКА, ОРЕЛ И РЕШКИ, КАМЕНЬ НОЖНИЦЫ БУМАГА.
# ЭТОТ КОД ИЗБЫТОЧЕН, Т.К. ПОВТОЯРЕТСЯ

# class Game:
#     @property
#     def rock_paper_scissors(self):
#         return choice(["rock", "paper", "scissors"])
#
#     @property
#     def flip(self):
#         return choice(["Heads", "Tails"])
#
#     @property
#     def dice(self):
#         return choice(range(1, 7))


# d = Game()
#
# for i in range(3):
#     print(d.dice)
#
# print(d.flip)
# print(d.flip)
# print(d.flip)



# ЗАПИШЕМ КОРОТКИЙ КОД С ПОМОЩЬЮ ДИСКРИПТОРА ДЛЯ ТЕХ ЖЕ ТРЕХ ИГР
class Choice:
    def __init__(self, *choice):
        self._choice = choice

    def __get__(self, obj, owner):
        return choice(self._choice)

class Game:
    dice = Choice(1, 2, 3, 4, 5, 6)
    flip = Choice("Heads", "Tails")
    rock_paper_scissors = Choice("rock", "paper", "scissors")


g = Game()

print(g.flip)
print(g.flip)
print(g.dice)
