from inspect import signature


def currying(func):
    def wrapper(*args):
        count = len(signature(func).parameters)
        if count == len(args):
            return func(*args)
        print("Nothing")
    return wrapper
