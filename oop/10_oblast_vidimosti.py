

class Person:
    name = "Dima"
    @classmethod # декоратор @classmethod, получает сам класс как обьект.
    # В переменную будет записан не экземпляр класса, а сам класс.
    # Глобальный для всех методов класса. Не имеет доступа к пространству имен экземпляров.
    def change_name(cls, name):
        cls.name = name

p = Person()
print(p.__dict__)
p.change_name("sfsdfgdgs")

print("instance dict", p.__dict__)
print("Person.name", Person.name)