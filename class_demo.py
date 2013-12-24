# -- coding: utf-8 --

class ClassDemo:

    def a():
        print "function a()"

    def b(self):
        print "function b()"

    @staticmethod
    def c():
        print "function c()"

    @classmethod
    def d(cls):
        print "function d()"


c = ClassDemo()

# c.a()
# TypeError: a() takes no arguments

c.b()
c.c()
c.d()

# ClassDemo.a()
# ClassDemo.b()
# TypeError: unbound method a() must be called with 
# ClassDemo instance as first argument (got nothing instead)

ClassDemo.b(c)
ClassDemo.c()
ClassDemo.d()