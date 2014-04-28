# -- coding: utf-8 --

import re

# # 将正则表达式编译成Pattern对象
# pattern = re.compile(r'^1[3,4,5,8][0-9]{9}')

# # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
# m1 = pattern.match('110')
# print m1


# # if match:
# #     # 使用Match获得分组信息
# #     print match.group()

# ### 输出 ###
# # hello

# m2 = pattern.match('15026612137')
# print m2

# m3 = pattern.match('18626612137')
# print m3

# m4 = pattern.match('18926612137')
# print m4

# m5 = pattern.match('11626612137')
# print m5


# m6 = pattern.match(u'13626612137')
# print m6



# pattern1 = r"[\w\u4e00-\u9fa5]{2,16}$"

# p1 = re.compile(pattern1)
# s1 = p1.match(name_correct)
# print "s1 {}".format(s1)
# if not s1:
#     print u"{} error".format(name_correct)

# p2 = re.compile(pattern1)
# s2 = p2.match(name_error)
# print "s2 {}".format(s2)
# if not s2:
#     print u"{} error".format(name_error)


pattern1 = u'^[_a-zA-Z0-9\u4e00-\u9fa5]{2,16}$'


correct_names = [
    u"abcd",
    u"123456",
    u"test_1234",
    u"阿赐test_1234"
]

for name in correct_names:
    if not re.search(pattern1, name):
        print u"{} error".format(name)
    else:
        print u"{} correct".format(name)


error_names = [
    u"\阿赐test_1234-@^.。：~",
    u"$阿赐test_1234-@^.。：~",
    u"(阿赐test_1234-@^.。：~",
    u"1",
    u"123456789abcdefghjklqwertyui"
]


for name in error_names:
    if not re.search(pattern1, name):
        print u"{} error".format(name)
    else:
        print u"{} correct".format(name)
