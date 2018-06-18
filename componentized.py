def componentized(cls):
    class WrappedClass:
        def __init__(self, *args):
            self.wrapped_instance = cls(*args)
            self.components = []
            for i in cls.__dict__:
                if type(cls.__dict__[i]) == Component:
                    self.components.append(i)

        def __getattr__(self, name):
            attr_list = self.__checkattr(name)
            if len(attr_list) == 1:
                return getattr(self.wrapped_instance, name)
            return tuple(getattr(self.wrapped_instance, attr) for attr in attr_list)

        def __checkattr(self, name):
            ret = []
            for comp in self.components:
                if comp in name and not(comp in ret):
                    ret.append(comp)
            return ret

    return WrappedClass


class Component:
    def __init__(self, t):
        self.type = t
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if self.type != type(value):
            raise AttributeError("Type \"{}\" do not match \"{}\".".format(type(value), self.type))
        else:
            self.value = value


@componentized
class Color:
    r = Component(int)
    g = Component(int)
    b = Component(int)

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


c = Color(255, 200, 160)
print("\"{}\" \"{}\" \"{}\"".format(c.r, c.g, c.b))
print(c.rb)
