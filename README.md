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
    def __init
~~~