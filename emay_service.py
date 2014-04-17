# -- coding: utf-8 --

import urllib2
from xml.etree import ElementTree

# http://sdk999ws.eucp.b2m.cn:8080/sdkproxy//sendsms.action?
# cdkey=0SDK-EMY-0130-AAAAA&password=123456&phone=1333333333,13444444444&
# message=单发即时短信测试&addserial=10086

# 注：phone 多个电话用逗号“,“ 隔开
# Message 短信内容用UTF-8编码
# Addserial   附加码或置为空

# <?xml version="1.0" encoding="UTF-8"?><response><error>0</error><message></message></response>

# def parse_result(result):
#     print result
#     # this will give us the contents of the data tag.
#     error = XML(result).find("error").text
#     print error
#     print error.__class__

def parse_result(result):
    print result
    # this will give us the contents of the data tag.
    root = ElementTree.fromstring(result)

    node_find = root.find('error')

    print node_find
    print node_find.__class__
    print node_find.text


def send_sms(mobile, content):
    print mobile
    print content
    host = "http://sdk999ws.eucp.b2m.cn:8080/sdkproxy//sendsms.action"
    cdkey = "YourKey"
    password = "YourPassword"

    url = "{}?cdkey={}&password={}&phone={}&message={}".format(host,
        cdkey, password, mobile, content.encode('utf8'))
    print url

    result = urllib2.urlopen(url).read()
    print result

    #parse_result(result)

code = 111111
message_template = u"走走验证码：{}（30分钟内有效），仅用于注册不能重复使用，为了账号安全请勿告知他人。【走走】"
content = message_template.replace("{}", unicode(code))

mobile = "15026612137"

#send_sms(mobile, content)

result = '<?xml version="1.0" encoding="UTF-8"?><response><error>0</error><message></message></response>'
parse_result(result)
