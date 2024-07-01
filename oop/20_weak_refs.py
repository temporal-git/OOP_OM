# СЛАБЫЕ ССЫЛКИ


import weakref

class Person:
    pass


p = Person()
w = weakref.ref(p)

print(w)
print(hex(id(p)))
print(w())

del p
print(w)
print(w())



p = Person()
d = weakref.WeakKeyDictionary()
print(d)
d[p] = 10
print(d[p])
print(dir(d))

print(d.keyrefs())

del p

print(d.keyrefs())


p = Person()
print(hash(p))