# -- coding: utf-8 --

import math

# 分割符方法
def dash(str=''):
  print "-"*50
  if not str.isspace():
    print str


dash('callable to test method')
parameter = 1
foo_method = math.sqrt
print 'test parameter %s' %callable(parameter)
print 'test method %s' %callable(foo_method)


dash('method return value')
def foo_return(name):
  ret = 'Hi, %s.' %name
  return ret

print 'Should return: Hi, Henry.'
print foo_return('Henry')


dash('famous fibs function')
def fibs(num):
  result = [0, 1]
  for i in range(num-2):
    result.append(result[-2] + result[-1])
  return result

print 'test fibs 10: %s' %fibs(10)


dash("test change parameters")
def test_string(str):
  str = 'new'
  print "method-in string: %s" %str

old_string = 'old'
print 'init string: %s' %old_string
test_string(old_string)
print 'final string: %s' %old_string

def test_list(lis):
  lis[0] = 'new'
  print "method-in list: %s" %lis

old_list = ['old', 'hi']
print 'init list: %s' %old_list
test_list(old_list)
print 'final list: %s' %old_list


dash('copy list [:]')
print "old list %s" %old_list
l = old_list
print "l is old_list %s" %(l is old_list)
g = old_list[:]
print "g is old_list %s" %(g is old_list)


dash('default parameter value')
def default_param(name='Henry', age='26'):
  print 'Name: %s, Age: %s' %(name,age)

print "no parameters ():"
default_param()
print "one parameters ():"
default_param('Alice')
print "full parameters ():"
default_param('James', 25)


dash('any parameters')
def any_param(title, *params, **keyvalue):
  print title
  print params
  print keyvalue

print "any_param('First')"
any_param('First')

print "any_param('Second', 26)"
any_param('Second', 26)

print "any_param('Third', 26, 20, name='Henry', age=26)"
any_param('Third', 26, 20, name='Henry', age=26)

dash('external parameter')
def test_external(param):
  print param + name

name = 'Henry'
test_external('Name:')

dash('global parameter')
def test_global(name):
  print name + globals()['name']

name = 'Alice'
test_global('Name:')

dash('recursive method')
def count_number(number):
  ret = number
  for i in range(1, number):
    ret *= i
  return ret

print "4 recursive count: %s" %count_number(4)

def count_number_v2(number):
  if number == 1:
    return number
  else:
    return number * count_number_v2(number - 1)

print "5 recursive count: %s" %count_number_v2(5)

