# -- coding: utf-8 --

# 分割符方法
def dash(str=''):
  print "-"*50
  if not str.isspace():
    print str

dash("数组")
colors = ["red", "yellow", "blue"]
print colors
print "list length: %d" %len(colors)
print "first element: %s" %colors[0]
print "index blue: %s" %colors.index('blue')

print "\nsort list"
colors.sort()
print colors

print "\nreverse list"
colors.reverse()
print colors

print "\nappend green to list"
colors.append("green")
print colors

print "\nremove red from list"
colors.remove("red")
print colors

print "\ninsert black into list"
colors.insert(0,"black")
print colors

print "\npop element in list"
colors.pop()
print colors

dash("for and in method for list/collection")
for color in colors:
  print color

if 'red' in colors:
  print "red in colors"

dash("range function return list")
for i in range(3):
  print i

dash("xrange function return a value")
for i in xrange(3):
  print i

dash ("while loop")
i = 1
while i < 5:
  print i
  i = i + 1

print "loop continue and break"
i = 0
while 1:
  i += 1
  if i % 2 == 0:
    print i
  if i == 10:
    break

dash('lish comprehensions')
print "[expression for variable in list]"
print "[expression for variable in list if condition]"
numbers = [1,2,3,4,5]
print [i*2 for i in numbers if i%2 == 0]

dash