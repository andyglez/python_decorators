def componentized(cls):
    class WrappedClass:
        def __init__(self, *args):
            self.__dict__['wrapped_instance'] = cls(*args)
            self.__dict__['components'] = []
            for i in cls.__dict__:
                if type(cls.__dict__[i]) == Component:
                    self.components.append(i)

        def __getattr__(self, name):
            attr_list = self.checkattrs(name)
            if len(attr_list) == 1:
                return getattr(self.wrapped_instance, name)
            return tuple(getattr(self.wrapped_instance, attr) for attr in attr_list)

        def __setattr__(self, name, value):
            attr_list = self.checkattrs(name)
            if isinstance(value, tuple):
                for attr, val in zip(attr_list, value):
                    setattr(self.wrapped_instance, attr, val)
            else:
                if len(attr_list) > 1:
                    for attr in attr_list:
                        setattr(self.wrapped_instance, attr, value)
                else:
                    setattr(self.wrapped_instance, name, value)

        def checkattrs(self, name):
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
