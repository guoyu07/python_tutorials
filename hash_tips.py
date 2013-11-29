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