# -- coding: utf-8 --

# 分割符方法
def dash(str=''):
  print "-"*50
  if not str.isspace():
    print str

# 字符
dash("字符")
print "Hello world"

# 数字

# 整型
dash("整型")
print 2
print -3

# 浮点
dash("浮点")
print 2.0

# 基本运算符和函数
# 数字运算符
# 求和
dash("数字运算符：求和")
print "2 + 2"
print 2 + 2

# 差值
dash("数字运算符：差值")
print "2 - 1"
print 2 - 1
 
# 相除
dash("数字运算符：相除")
print "1 / 2"
print 1 / 2

print "1.0 / 2.0"
print 1.0 / 2.0

print "1.0 // 2.0"
print 1.0 // 2.0

print "10.0 // 3.0"
print 10.0 // 3.0

# 取余
dash("数字运算符：取余")
print "3 % 2"
print 3 % 2

# 乘方
dash("数字运算符：乘方")
print "2 ** 2"
print 2 ** 2

print "(-3) ** 2"
print (-3) ** 2

print "pow(2,3)"
print pow(2,3)

print "pow(-3,2)"
print pow(-3,2)

# 一个组合运算
dash("一个组合运算")
print "1 + pow(2, 3*4)/5.0"
print 1 + pow(2, 3*4)/5.0

# 转换为整数
dash("转换为整数")
print "int(2.13)"
print int(2.13)

# 转换为浮点数
dash("转换为浮点数")
print "float(12)"
print float(12)


# 绝对值
dash("绝对值")
print "abs(-2)"
print abs(-2)

# 四舍五入
dash("四舍五入")
print "round(1.0/3.0)"
print round(1.0/3.0)

# 其他数学函数
dash("引入 math 模块")
print "import math"
import math

print "math.floor(1.23)"
print math.floor(1.23)

print "math.ceil(1.23)"
print math.ceil(1.23)

print "from math import sqrt"
print "sqrt(4)"
from math import sqrt
print sqrt(4)

# 还有一种夸张的用法
print "foo = math.ceil"
print "foo(1.23)"
foo = math.ceil
print foo(1.23)

# 看看 Python 的异常
dash("Python 的异常")
# print "方法不存在"
# error_funtion()

print "除以 0 "
print 2 / 0

