from inspect import signature


def currying(func):
    def wrapper(*args):
        count = len(signature(func).parameters)
        total_args = [x for x in args]
        if count == len(args):
            return func(*args)

        def curried(*new_args):
            for i in new_args:
                total_args.append(i)
            if len(total_args) < count:
                return curried
            return func(*tuple(x for x in total_args))
        return curried
    return wrapper
