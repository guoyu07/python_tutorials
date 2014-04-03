# -- coding: utf-8 --

import urllib2
#import sys


# esms2.etonenet.com/sms/mt 移动线路

# esms3.etonenet.com/sms/mt 联通线路

# esms4.etonenet.com/sms/mt 电信线路


def _result_to_hash(result):
    content = {}
    if result:
        parameters = result.split('&')
        for parameter in parameters:
            key,value = parameter.split('=')
            content[key] = value
    return content


def _parse_result(result):
    if result:
        params = _result_to_hash(result)
        print params
        mtstat = params.get('mtstat')
        print mtstat
        mterrocde = params.get('mterrocde')
        print mterrocde
        if mtstat == "ACCEPTD" and mterrocde == "000":
            return True
        else:
            print "errors"
            print params
    else:
        print "unknow result"


def send_sms(mobile, content):
    host = "http://esms2.etonenet.com/sms/mt"
    command = "MT_REQUEST"
    da = mobile
    gbk_content = content.encode('gbk')
    sm = gbk_content.encode('hex')
    #.encode('utf8')

    url = "{}?command={}&spid={}&sppassword={}&da={}&sm={}&dc=15".format(
        host, command, spid, sppassword, da, sm)
    print url

    result = urllib2.urlopen(url).read()
    print "=="*50
    print result

    _parse_result(result)



code = 123456
message_template = u"走走验证码：{}（30分钟内有效），仅用于注册不能重复使用，为了账号安全请勿告知他人。"
content = message_template.replace("{}", unicode(code))


send_sms('8615026612137', content)

# code = 1234
# content = u"走走验证码：{}（30分钟内有效），仅用于注册不能重复使用，为了账号安全请勿告知他人【走走】。"
# content = content.replace("{}", unicode(code))
# print content


# print sys.getdefaultencoding()
# ascii

# s1 = u'测试短信通道02。'

# s1 = '测试短信通道02。'
# print type(s1)

# ts = s1.decode( 'unicode-escape' )

# us = s1.encode("utf-8")
# print type(us)

# s1 = unicode('测试短信通道02。')
# ts = unicode(s1)
# print type(ts)


# s2 = ts.encode('gbk')
# s3 = s2.decode('gbk')

#s2 = unicode(s1,'gbk')
# s3 = s1.decode('gbk')
# s3 = s1.encode('gbk', 'ignore')

# print s1

# print ts

# print s2
# print s3

# send_sms('8615026612137', u'测试短信通道01。')
# send_sms('8618501618187', u'测试短信通道02。')

# def parse_content(content):
#     result = {}
#     if content:
#         parameters = content.split('&')
#         for parameter in parameters:
#             key,value = parameter.split('=')
#             result[key] = value
#     return result


# content = "command=MT_RESPONSE&spid=7943&mtmsgid=13962330346464666&mtstat=ACCEPTD&mterrcode=000"
# print parse_content(content)