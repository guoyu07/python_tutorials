# -- coding: utf-8 --

# 分割符方法
def dash(str=''):
  print "-"*50
  if not str.isspace():
    print str

names = [u'henry', u'\u6d77\u87ba\u58f3']
print type(names)
print names
join_str = u'、'
print join_str
print type(join_str)
join_name = join_str.join(names)
print type(join_name)

print join_name


dict1 = [{'id': '5'}, {'type': '2', 'name': '28\\u8def'}, {'id': '7'}, {'type': '3', 'name': '82\\u8def'}]
print dict1
print dict1[1]['name']
name = dict1[1]['name']
print name
print unicode(name)