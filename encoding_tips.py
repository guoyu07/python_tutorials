# -- coding: utf-8 --

# 分割符方法
def dash(str=''):
  print "-"*50
  if not str.isspace():
    print str

names = [u'henry', u'\u6d77\u87ba\u58f3']
print type(names)
print names
join_str = '、'
print join_str
print type(join_str)
join_name = join_str.join(names)
print type(join_name)

print join_name