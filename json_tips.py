# -- coding: utf-8 --

import json

class JsonTips(object):
    @staticmethod
    def test():
        # file = open("./doc/json_file.json", 'w')
        # data = {"user": {"name":"Henry", "age": 23}}
        # json_data = json.dumps(data)
        # file.write(json_data)
        # file.close()

        # {"user": {"age": 23, "name": "Henry"}}

        data = {"user": {"name":"Henry", "age": 23}}
        with open('./doc/json_file.json', 'a') as outfile:
            json.dump(data, outfile, indent=2)

        # {
        #   "user": {
        #     "age": 23,
        #     "name": "Henry"
        #   }
        # }


JsonTips.test()
print "Done"