# Python Decorators

The act of decoration, in Python at least, is a way to specify management or augmentation code for functions and classes.
Decorators themselves take the form of callable objects that process other callable objects.

They are a way to do name rebinding at function or class definition time in which provide another layer of logic to manage
them whether is function to be called later, or an instance of a class created by it.

In typical use this works as a wrapper for its definition in way to intercept function calls or to intercept instance
creation calls and process them as needed; but this isn't the only way decorators can be used. They can be used to manage
function objects and their register to an API or to manage class objects directly which is a topic related with programming
metaclasses.

~~~py
@currying
def add(p, q, r, s):
    return p + q + r + s
~~~

This is an example of typical use as a function wrapper adding some code to the function definition and renaming it.

~~~py
def currying(func):
    def wrapper(*args):
        # Enables currying (as it name indicates)
    return wrapper
~~~

As shown, decorator returns another callable object in a way that it is still possible to call with the name of the original
function but now is little more than that. Finally, thanks to the decorator it is now possible to use another feature that
isn't part of the original Python language and now is possible to do the next calls without any kind error:

~~~py
add(1,2)(3,4)       # 10
add(10)(20)(30)(40) # 100
~~~

## Managed Attributes ##

It is one of the fundamentals of Python's core, the attribute interception is the main point of decision in the behavior
of an instance of a class. In most cases, an object's attributes lives within its definition or it is inherited from a
parent class, but, sometimes, more flexibility is required so the object will mutate and the class must be prepared for
the change.

**Property**

This protocol allows to route a specific attribute's get and set or intercept attribute access, intercept delete operations
and provide documentation. A property manages a single specific attribute, that is it can't catch all attribute accesses.

~~~py
attribute = property(fget, fset, fdel, doc)
~~~

With the use of python decorators is now possible to declare a function decorated as a property which will make it behave
exactly as a property and also the accessors can be decorated to work for that specific property.

~~~py
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

~~~

**Descriptors**

They provide an alternative way to intercept attribute access. Functionally speaking it allows us to route a specific
attribute access operation to methods of a separate class' instance object, previously specified. Descriptors are created
as independent classes and are assigned to class attributes just like method functions.

Unlike properties, descriptors are broader in scope, and provide a more general tool. For instance, because they are coded
as normal classes, descriptors have their own state, may participate in descriptor inheritance and hierarchies, can use
composition to aggregate objects, and provide a natural structure for coding internal methods and attribute documentation
strings.

~~~py
class Descriptor:
    "Doc string for descriptor"                  # documentation string
    def __get__(self, instance, owner): ...     # getter: returns attr value
    def __set__(self, instance, value): ...     # setter: returns None (Nothing)
    def __delete__(self, instance): ...          # delete: returns None (Nothing)
~~~

Their definitions are the ones to decide its characteristics, that is, if descriptor only has a definition of a getter
then it is read-only, if only a setter it is write-only. But it is still not enough since a parent class can hide its
property.

A descriptor state is used to manage either data internal to the workings of the descriptor, or data that spans all instances.
It can vary per attribute appearance.

An instance state records information related to and possibly created by the client class. It can vary per client class instance.

**__getattr__**

It is part of Python's general overloading protocol, that is, unlike properties and descriptors. They are also broader because
their are the core of attribute access which allows it to have a delegation-based coding patterns.

They are part of the class' definition and because of that they are also involved with inheritance, so it is a potential
recursive call between itself and a parent definition, but the stronger case is when __setattr__ is also defined and a
trick must be made to avoid such recursion problems: whenever setting an attribute is better to do it through the object's
field dictionary to avoid direct attribute assignment.

~~~py
class Component:                    # Example of a descriptor
    def __init__(self, t): ...              # Describes an object and its type

    def __get__(self, instance, owner): ... # getter access control

    def __set__(self, instance, value): ... # setter access control
        # After type checking assign its value
~~~

~~~py
def componentized(cls):                 # Structure of a class decorator
    class WrappedClass:
        def __init__(self, *args):
            # Trick to avoid recursion within __getattr__
            self.__dict__['wrapped_instance'] = cls(*args)
            self.__dict__['components'] = []
            # ... Assign described class components to list of components

        def __getattr__(self, name): ...        # Attribute getter control

        def __setattr__(self, name, value): ... # Attribute setter control

    return WrappedClass
~~~

Now, componentized can be used as a decorator, which is a class containing a decorated class that controls access (get or set)
to its members, specialized with component members to describe their access further more.
