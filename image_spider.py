# -- coding: utf-8 --

import re
import urllib
import urllib2

from random import randint
from time import sleep

from os.path import basename
from urlparse import urlsplit

class ImageSpider:

  def fetch(self):
    file = open("./doc/college_names.txt", 'r')
    for line in file:
      name = line.strip()
      print "Search image for %s" %name

      url = "http://cn.bing.com/images/search?q=%s&go=&qs=n&form=QBIR&pq=%s&sc=8-4&sp=-1&sk=" %(name, name)
      html = urllib2.urlopen(url).read()
      #print "Html result %s" %html

      images = re.findall(r'<img src="http://(.*?)>', html)
      self.save_images(name, images)
      sleep(randint(1,3))

    file.close()

  def save_images(self, name, images):
    index = 0
    for image in images:
      if index < 3:
        index += 1
        end_src = image.index('"')
        image_url = "http://" + image[0:end_src]
        image_name = "./doc/images/" + name + str(index) + ".jpg"
        print "image_url %s" %image_url
        print "image_name %s" %image_name
        urllib.urlretrieve(image_url, image_name)
      else:
        break

  def url2name(self, url):
      return basename(urlsplit(url)[2])

  def split_url(self, url):
      print url
      print self.url2name(url)


# ImageSpider().fetch()

image = "http://api.dev.test1.demo.org.cn/uploads/76/de/76de3eb753a81f24038cbc0d4f34bba9.jpg"
ImageSpider().split_url(image)