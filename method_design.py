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


