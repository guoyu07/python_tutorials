# -- coding: utf-8 --

class PrintUtil(object):
  pass

  # 分割符方法
  def dash(str):
    print "-"*50
    print str

class PrintUtil:
  content = "Default content"

  # 分割符方法
  def dash(self, content):
    print "-"*50
    print self.content

print_util = PrintUtil()
dash = print_util.dash('')