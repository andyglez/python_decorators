def componentized(cls):
    class WrappedClass(object):
        def __init__(self, *args):
            self.__dict__['wrapped_instance'] = cls(*args)
            self.__dict__['components'] = []
            for i in cls.__dict__:
                if type(cls.__dict__[i]) == Component:
                    self.components.append(i)
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
