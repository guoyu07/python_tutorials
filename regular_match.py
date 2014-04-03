# -- coding: utf-8 --

import re

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'^1[3,4,5,8][0-9]{9}')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
m1 = pattern.match('110')
print m1


# if match:
#     # 使用Match获得分组信息
#     print match.group()

### 输出 ###
# hello

m2 = pattern.match('15026612137')
print m2

m3 = pattern.match('18626612137')
print m3

m4 = pattern.match('18926612137')
print m4

m5 = pattern.match('11626612137')
print m5


m6 = pattern.match(u'13626612137')
print m6