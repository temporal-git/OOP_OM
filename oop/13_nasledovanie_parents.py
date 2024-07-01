
class IntelCpu:
    cpu_socket = 1151
    name = "Intel"

class I7(IntelCpu):
    pass

class I5(IntelCpu):
    pass






i5 = I5()
i7 = I7()
print(isinstance(i5, IntelCpu)) # is instance проверяет принадлежит ли i5 классу IntelCpu
# проверяет по всему дереву наследования
# выдаст True

print(type(i5))

class One:
    pass

class Two(One):
    pass

class Three(Two): # Родитель у класса моет быть только один, для three это Two. Но предков может быть больше, это и Two и One
    pass

print(issubclass(Three, One)) # выдаст True, понимает только классы.
# с экземплярами не работает
print(isinstance(i5, type(i7))) # выдаст False
print(issubclass(type(i5), type(i7))) # выдаст False