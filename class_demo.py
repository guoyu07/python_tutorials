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


class Plan(object):

    def __init__(self, content=None):
        if content is None:
            content = {}
        self.foods = content.get("foods", {})
        self.hotels = content.get("hotels", {})

    def prepare_foods(self):
        if len(self.foods["want"]) < 2:
            self.foods["want"].append(11)

    def prepare_hotels(self):
        if len(self.hotels["want"]) < 2:
            self.hotels["want"].append(28)

    @staticmethod
    def build(content):
        plan = Plan(content)
        plan.prepare_foods()
        plan.prepare_hotels()
        return plan


content = {"hotels":{"must":[164],"want":[165]},
    "foods":{"must":[183],"want":[184]}}

plan = Plan.build(content)
print plan.foods
print plan.hotels

content2 = {"hotels":{"must":[164],"want":[165, 1]},
    "foods":{"must":[183],"want":[184, 2]}}

plan2 = Plan.build(content2)
print plan2.foods
print plan2.hotels







