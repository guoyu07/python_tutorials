# -- coding: utf-8 --

class SwitchDemo(object):
    def __init__(self, day=None):
        self.day = day or 1

    def func1(self):
        if self.day == 1:
            tag = "上午"
        else:
            tag = "第一天"
        return tag

    def func2(self):
        if self.day == 1:
            tag = "中午"
        else:
            tag = "第二天"
        return tag

    def func3(self):
        if self.day == 1:
            tag = "下午"
        else:
            tag = "第三天"
        return tag

    def switch_case(self, period):
        return {
            1: lambda: self.func1(),
            2: lambda: self.func2(),
            3: lambda: self.func3()}[period]()

print SwitchDemo(1).switch_case(1)
print SwitchDemo(1).switch_case(3)

print SwitchDemo(2).switch_case(1)
print SwitchDemo(2).switch_case(2)
