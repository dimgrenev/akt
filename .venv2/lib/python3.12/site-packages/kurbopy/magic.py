import functools
import sys


# This module allows for polymorphic operator overloading between objects of
# different classes without driving Rust's type system mad. When a magic method
# (eg. __add__) is called on a Rust object, the Rust object will call
# `kurbopy.magic.magic_add(self, rhs)`. This will in turn look up a method on
# the Rust object, `_add_Rhs`, where `Rhs` is the class name of the rhs object.
# If this method is not found, a TypeError is raised.


def get_magic_name(obj):
    cls = obj.__class__
    if hasattr(cls, "__name__"):
        return cls.__name__
    raise ValueError("No magic name for " + str(obj))


def do_magic(self, rhs, methodname):
    other_type = get_magic_name(rhs)
    if hasattr(self, "_" + methodname + "_" + other_type):
        return getattr(self, "_" + methodname + "_" + other_type)(rhs)
    mytype = get_magic_name(self)
    raise TypeError("Cannot %s %s by %s" % (methodname, mytype, other_type))


for method in ["mul", "add", "sub", "isub", "iadd"]:
    magic = functools.partial(do_magic, methodname=method)
    magic.__name__ = method
    magic.__doc__ = "Magic method " + method
    globals()["magic_" + method] = magic

