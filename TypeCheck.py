class TypeCheck:
    def __init__(self, *types):
        self.types = types

    def __call__(self, func):
        def wrapper(*args):
            for i in range(len(args)):
                assert isinstance(args[i], self.types[i]), ("Type Error, parameter {0} expected to be of type {1} but has {2}".format(i, self.types[i], type(args[i])))
            return func(*args)
        return wrapper


def typecheck(*types):
    def decorator(func):
        def wrapper(*args):
            for i in range(len(args)):
                assert isinstance(args[i], types[i]), ("Type Error, parameter {0} expected to be of type {1} but has {2}".format(i, types[i], type(args[i])))
            return func(*args)
        return wrapper
    return decorator
