# -- coding: utf-8 --

class ImageSpider:

  @classmethod
  def fetch(cls):
    file = open("./doc/college_names.txt", 'r')
    for line in file:
      print line
    file.close()

ImageSpider.fetch()