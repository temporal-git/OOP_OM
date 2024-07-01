

class ValidString:
    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        print("__set__() was called")
        if not isinstance(value, str):
            raise ValueError(f"{self.property_name} must be a String, but {type(value).__name__} was passed")
        # key = "_" + self.property_name
        # setattr(instance, key, value)
        instance.__dict__[self.property_name] = value # можно без сеттора / геттора сделать

    def __get__(self, instance, owner):
        print("__get__() was called")
        if instance is None:
            return self
        # key = "_" + self.property_name
        # return getattr(instance, key, None)
        return instance.__dict__.get(self.property_name, None) # тоже рабоатет


class Person:
    name = ValidString()
    surname = ValidString()


p = Person()
p.name = "ivan"
# p.surname = 123 # выдаст ошибку

print(p.__dict__)
print(p.name)
