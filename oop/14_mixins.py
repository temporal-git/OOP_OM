# можем с помощью миксина подмешать любимую еду другому несвязанному классу, например собачкам

class FoodMixin:
    food = None

    def get_food(self):
        if self.food is None:
            raise ValueError("Food should be set")
        print(f"I like {self.food}")

class Person:
    def hello(self):
        print("Im Person")

class Student(FoodMixin, Person):
    food  = "Pizza"
    def hello(self):
        print("Im Student")


s = Student()

s.get_food()
