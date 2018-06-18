from componentized import componentized
from componentized import Component

from currying import currying


@componentized
class Color:
    a = Component(int)
    r = Component(int)
    g = Component(int)
    b = Component(int)

    def __init__(self, a, r, g, b):
        self.a = a
        self.r = r
        self.g = g
        self.b = b


@currying
def add(p, q, r, s):
    return p + q + r + s

c = Color(23, 255, 200, 160)
print("\"{}\" \"{}\" \"{}\" \"{}\"".format(c.a, c.r, c.g, c.b))
c.argb = 255
print(c.argb)
c.argb = (0, 0, 0, 0)
print(c.argb)

print("\n==========================\n")

print(add(1, 2, 3))
