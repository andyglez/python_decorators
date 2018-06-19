from componentized import componentized
from componentized import Component

from currying import currying

from TypeCheck import TypeCheck
from TypeCheck import typecheck


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


@TypeCheck(str, str)
def concat(x, y):
    return x + y


@typecheck(str, str)
def my_concat(x, y):
    return x + y


class Memoize:
    def __init__(self, func):
        self.func = func
        self.memory = {}

    def __call__(self, *args):
        if not(args in self.memory):
            self.memory[args] = self.func(*args)
        return self.memory[args]


@Memoize
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

c = Color(23, 255, 200, 160)
print("\"{}\" \"{}\" \"{}\" \"{}\"".format(c.a, c.r, c.g, c.b))
c.argb = 255
print(c.argb)
c.argb = (0, 0, 0, 0)
print(c.argb)

print("=" * 20)

print(add(1)(2, 3, 4))
print(concat("hello, ", "andy"))
print(my_concat("hello, ", "andy"))

print(fib(4))
