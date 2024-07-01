class Person:
    def create(self):
        self.name = "Ivan"

    def display(self):
        print(self.name)


p = Person()  # p.display() # выдаст ошибку, т.к. локальный словарь экземпляра p пустой и атрибутов у экземпляра по умолчанию нет.
print(p.__dict__)


# чтобы оно появилось нужно или вручную прописывать через .name или запускать функцию create:
# p.create()
# print(p.__dict__)
# что может быть неудобно

# Поэтому для задания свойств при создании экземпляра класса и присваивания ему начальных значений, инициализации, существует метод init
# Метод __init__ называют конструктором класса, что не совсем верно, т.к. изначально вызывается метод __new__() что и есть конструктор класса,
# а __init__ служит для инициализации.

class Person:
    def __init__(self,
                 name):  # будет вызываться автоматически при создании экземпляра, и нужные свойства добавятся автоматически тоже
        self.name = name

    def display(self):
        print(self.name)


p = Person("Ivan")
print(p.name)
print(p.__dict__)
