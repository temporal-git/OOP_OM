# полиморфизм это когда один метод по разному работает для разных классов
# например сложение числе и сложение строк

class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def __add__(self, room_obj): # переопределим работу встроенного оператора + или __add__
        if isinstance(room_obj, Room):
            return self.area + room_obj.area
        raise TypeError("Wrong object")

    def __eq__(self, room_obj): # переопределим работу встроенного оператора сравнения
        if self.area == room_obj.area:
            return True
        return False


r1 = Room(3, 5)
r2 = Room(4, 7)


print(r1.area)
print(r2.area)
print(r1 + r2)
print(r1 == r2)
