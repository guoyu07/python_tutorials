# -- coding: utf-8 --

# 分割符方法
def dash(str=''):
  print "-"*50
  if not str.isspace():
    print str


dash('字典')

ebooks = {}
print "Empty dictionary %s" %ebooks

ebooks['Ruby'] = 'Matz'
ebooks['Python'] = 'Guido'
ebooks['Java'] = 'James'

print "Ebooks dictionaries %s" %ebooks

dash('读取数据')

print 'keys()'
print 'Ebooks keys %s' % ebooks.keys()

print 'values()'
print 'Ebooks values %s' % ebooks.values()

print 'iterate items'
for key,value in ebooks.iteritems():
  print "Ebooks name %s and author %s" %(key, value)


dash('删除数据')
print 'del()'
del(ebooks['Java'])
print "Ebooks dictionaries %s" %ebooks

print 'pop()'
ebooks.pop('Ruby')
print "Ebooks dictionaries %s" %ebooks


dash('sorted list of dict by lower string')
data = [{"pinyin": "asc"},
    {"pinyin": "abc"},
    {"pinyin": "henry"},
    {"pinyin": "jack"},
    {"pinyin": "des"}]
print data
sortedlist = sorted(data, key=lambda k: k['pinyin'])
print "sorted list is: %s" %sortedlist


dash('sorted list of dict by pinyin')
provinces = [{"pinyin": "SHANGHAI"},
    {"pinyin": "JIANGSU"},
    {"pinyin": "FUJIAN"},
    {"pinyin": "HEILONGJIANG"},
    {"pinyin": "ANHUI"}]
print data
newlist = sorted(provinces, key=lambda k: k['pinyin'])
print "sorted list is: %s" %newlist


dash('creates a new dictionary with keys from seq and values set to value.')
days = 3
s1 = dict.fromkeys(xrange(days))
# >>> s1
# {0: None, 1: None, 2: None}

s2 = dict.fromkeys(xrange(days), [])
# >>> s2
# {0: [], 1: [], 2: []}
