# -- coding: utf-8 --

english = 'henry'
chinese = '你好'
u_chinese = u'\u6d77\u87ba\u58f3'

print english
print type(english)

print chinese
print type(chinese)

print u_chinese
print type(u_chinese)



# 分割符方法
# def dash(str=''):
#   print "-"*50
#   if not str.isspace():
#     print str

# names = [u'henry', u'\u6d77\u87ba\u58f3']
# print type(names)
# print names
# join_str = u'、'
# print join_str
# print type(join_str)
# join_name = join_str.join(names)
# print type(join_name)

# print join_name


# dict1 = [{'id': '5'}, {'type': '2', 'name': '28\\u8def'}, {'id': '7'}, {'type': '3', 'name': '82\\u8def'}]
# print dict1
# print dict1[1]['name']
# name = dict1[1]['name']
# print name
# print unicode(name)

# # iphone emoji character
# dash("iphone emoji character")
# # str_emoji = "\xF0\x9F\x98\x84\xE5\x93..."
# #content = u'\U0001f604\u5c3c\u739b'
# content = '\U0001f604\u5c3c\u739b'
# print content

# replace_content = content.replace("\U", "[emoji]")
# print replace_content

# import cgi
# escaped_str = cgi.escape(content) # 这样又回到了 html = '&lt;abc&gt'
# print escaped_str


# import urllib

# quote_str = urllib.urlencode(content)
# print quote_str

# unquote_str = urllib.unquote(quote_str)
# print unquote_str

# # import base64
# import base64
# #encode_str = base64.encodestring(content)
# encode_str = base64.b64encode(content)
# print encode_str

# dencode_str = base64.decodestring(content)
# print dencode_str


# # escaped
# # 这样又回到了 html = '&lt;abc&gt'
# import cgi
# escaped_str = cgi.escape(content)
# print escaped_str


# # Python 2.x:
# # unescaped
# import HTMLParser
# html_parser = HTMLParser.HTMLParser()
# unescaped_str = html_parser.unescape(content)
# print unescaped_str

# How to replace a double backslash with a single backslash in python?

# content = '\U0001f604\u5c3c\u739b'
# # '\\U0001f604\\u5c3c\\u739b'
# print content
# # \U0001f604\u5c3c\u739b
# content.decode('unicode_escape')
# # \U0001f604\u5c3c\u739b
