# -- coding: utf-8 --

# 分割符方法
def dash(str=''):
  print "-"*50
  if not str.isspace():
    print str

str = "Say hello to string."
print str

dash("calculate str length len()")
print len(str)

dash("[index] to index string")
print str[0]

dash("[index:length] to split string")
print str[0:3]

dash("use + to plus two strings")
print str + " Ok, I got it."

dash("use \% to put together string. (%d int, %s string, %f/%g float)")
print "%d 本《%s》杂志" %(3,"程序员")

dash("获取用户输入")
language = raw_input("What programming Language do you prefer?")
if language.lower() == 'ruby':
  print "Really? I'm a Ruby guy."
else:
  print "OK. you like %s. But I like Ruby the most." %language

