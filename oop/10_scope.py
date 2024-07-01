
class Person:
    def __init__(self, name):
        self.name = name

    @classmethod # создадим "второй" init метод, который будет брать имя из файла
    def from_file(cls, path):
        with open(path) as f:
            name = f.read().strip()
        return cls(name=name)

    @classmethod # Создадим еще init метод, который будет брать имя из объекта, т.е. другого класса например
    def from_obj(cls, obj):
        if hasattr(obj, "name"):
            name =  getattr(obj, "name")
            return cls(name=name)
        return cls



p = Person("oleg")
print(p.__dict__)
print(p.name)

p = Person.from_file("C:\pythonPr\oop\ext.txt")
print(p.__dict__)
print(p.name)

class Config:
    name = "Igor"

p = Person.from_obj(Config)
print(p.__dict__)
print(p.name)
