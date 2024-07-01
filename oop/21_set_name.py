class ValidString:
    def __set_name__(self, owner_class, property_name):
        print(f"owner_class: {owner_class}")
        print(f"property_name: {property_name}")


class Person:
    name = ValidString() # произошло исполнение кода без вызова
