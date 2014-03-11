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

dash('Accessing Values in Lists')
init_list = [1,2,3,4,5]
print "init_list:", init_list
print "init_list[0]:", init_list[0]
print "init_list[-1]:", init_list[-1]
print "init_list[0:2]:", init_list[0:2]
print "init_list[2:4]:", init_list[2:4]
print "init_list[-2:-1]:", init_list[-2:-1]

dash('Loop list with index')
init_list = [19,87,11,28]
print "init_list:", init_list
for index, value in enumerate(init_list):
    print index, value

dash('Get proper resolution')
resolutions = [{"height": 800, "width": 480},
               {"height": 1280, "width": 800},
               {"height": 1920, "width": 1200}]

def proper_resolution(height, resolutions):
    resolution = resolutions[0]
    resolution_size = len(resolutions)
    for index, value in enumerate(resolutions):
        current_height = value["height"]
        if height <= current_height:
            if index == 0:
                  resolution = value
            else:
                  former = resolutions[index-1]
                  former_height = former["height"]
                  if (height - former_height) <= (current_height - height):
                      resolution = former
                  else:
                      resolution = value
            break
        else:
            if index + 1 == resolution_size:
                  resolution = value
                  break
    return resolution

print "resolutions:", resolutions
height = 600
print "height:", height
print "proper_resolution:", proper_resolution(height, resolutions)

height = 850
print "height:", height
print "proper_resolution:", proper_resolution(height, resolutions)

height = 1000
print "height:", height
print "proper_resolution:", proper_resolution(height, resolutions)

height = 1100
print "height:", height
print "proper_resolution:", proper_resolution(height, resolutions)

height = 1600
print "height:", height
print "proper_resolution:", proper_resolution(height, resolutions)

height = 1700
print "height:", height
print "proper_resolution:", proper_resolution(height, resolutions)

height = 2000
print "height:", height
print "proper_resolution:", proper_resolution(height, resolutions)
