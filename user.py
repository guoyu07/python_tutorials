# -- coding: utf-8 --

import sys

class User:
    # def __new__(cls, *args, **kwargs):
    #     print "__new__ called", cls, args, kwargs
    #     return object.__new__(cls)

    _city = "Shanghai"
    __home = "Jiangsu"

    def __init__(self, name):
        self.name = name
        print "__init__ called", name

    def __del__(self):
        print "__del__ called"


u = User("Henry")
print u.name

print u._city
print u._User__home

u2 = u
print sys.getrefcount(u2)

del u
print sys.getrefcount(u2)