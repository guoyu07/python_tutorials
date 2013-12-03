# -- coding: utf-8 --

from time import sleep

class ClassPerson:

  def __init__(self):
    print "This is a Persion"

  def greeting(self):
    print "Hi"

  def lifestyle(self):
    print "work"
    print "eat"
    print "sleep"


class ClassMale:

  def __init__(self):
    print "This is a Male"

  def greeting(self):
    print "Hey, buddy."

  def lifestyle(self):
    print "work"
    sleep(1)
    print "and work"
    print "and sleep"


class ClassFemale:

  def __init__(self):
    print "This is a Female"

  def greeting(self):
    print "Hi, honey."

  def lifestyle(self):
    print "work"
    print "and eat"
    print "and shopping"
    print "and eat"
    print "and watching tv"
    sleep(1)
    print "finally sleep"

p = ClassPerson()
p.greeting()
p.lifestyle()

print "-"*50
sleep(2)

m = ClassMale()
m.greeting()
m.lifestyle()

print "-"*50
sleep(2)

fm = ClassFemale()
fm.greeting()
fm.lifestyle()