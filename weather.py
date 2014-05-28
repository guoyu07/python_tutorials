import json
import urllib2


url = "http://weather.api.114la.com/2307/101230701.txt"

request = urllib2.Request(url)
content = urllib2.urlopen(url).read()

print content.__class__
print content


print content.find('{')
print content.rfind('}')

raw_data = content[content.find('{'):content.rfind('}')+1]

print raw_data

json_data = json.loads(raw_data)

print json_data
print json_data.__class__


print  json_data.get('weatherinfo').get('city')
print  json_data.get('weatherinfo').get('date')
print  json_data.get('weatherinfo').get('temp1')
print  json_data.get('weatherinfo').get('weather1')

# import re
# matchObj = re.match(r'^\{(.*)\}$', content, re.M|re.I)

# if matchObj:
#     print matchObj.group()
# else:
#     print "not match"

#urllib2.urlopen(request)

#json.load(urllib2.urlopen(request))
