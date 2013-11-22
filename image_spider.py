# -- coding: utf-8 --

import re
import urllib2

class ImageSpider:

  @classmethod
  def fetch(cls):
    file = open("./doc/college_names.txt", 'r')
    for line in file:
      name = line.strip()
      print "Search image for %s" %name

      url = "http://cn.bing.com/images/search?q=%s&go=&qs=n&form=QBIR&pq=%s&sc=8-4&sp=-1&sk=" %(name, name)
      html = urllib2.urlopen(url).read()
      #print "Html result %s" %html

      images = re.findall(r'<img(.*)>', html)
      index = 0
      for image in images:
        if index < 3:
          index += 1
          print image
        else:
          break

    file.close()

ImageSpider.fetch()