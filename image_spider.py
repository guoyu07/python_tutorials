# -- coding: utf-8 --

import re
import urllib
import urllib2

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
      index = 0

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

ImageSpider().fetch()