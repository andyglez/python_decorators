# Python Decorators

The act of decoration, in Python at least, is a way to specify management or augmentation code for functions and classes.
Decorators themselves take the form of callable objects that process other callable objects.

They are a way to do name rebinding at function or class definition time in which provide another layer of logic to manage
them whether is function to be called later, or an instance of a class created by it.

In typical use this works as a wrapper for its definition in way to intercept function calls or to intercept instance
creation calls and process them as needed; but this isn't the only way decorators can be used. They can be used to manage
function objects and their register to an API or to manage class objects directly which is a topic related with programming
metaclasses.


