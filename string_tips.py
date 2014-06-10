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

dash('use startswith()')
print "%s starts with 'Say': %s" %(str,str.startswith('Say'))

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

str1 = """first content"""
print str1 + """ second content"""
print """{}, test""".format("Hi")

dash("weather string")
temp = "23℃~32℃"
weather =  "阵雨转阴"

t_i = temp.find('℃')
if t_i > 0:
    print temp[0:t_i]
else:
    print "temp not contains ~"

w_i = weather.find('转')
if w_i > 0:
    print weather[0:w_i]
else:
    print "weather not contains ~"