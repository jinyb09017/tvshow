# coding:utf-8
import requests
import json


# cs_url = 'https://api.github.com'
# cs_user = 'jinyb09017'
# cs_psw = 'hundsun@1314'
#
# r = requests.get(cs_url, auth=(cs_user, cs_psw))
#
# if r.status_code == requests.codes.ok:
#     for k, v in r.json().items():
#         print k, v
class Http:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_key_new():
        print("是静态方法")

        cs_url = 'http://192.168.100.63:8080/codegen/tv_key.jsp'

        r = requests.post(cs_url)
        print r.content

        try:
            if r.status_code == requests.codes.ok:
                # content = r.content.decode('utf-8')
                content = r.content
                jsonObject = json.loads(content)
                print "ok"
                key = jsonObject['key']
                print key

                return key
            else:
                return ""
        except Exception, e:

            print e
            return ""

    @staticmethod
    def get_key(code):
        print("是静态方法")

        cs_url = 'https://tv.apitops.com/newtv/ValidateCode'
        # requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        payload = {"code": "486660"}
        payload['code'] = code
        print payload
        cert_file_path = "newfile.crt.pem"
        key_file_path = "newfile.key.pem"
        cert = (cert_file_path, key_file_path)
        r = requests.post(cs_url, data=payload, cert=cert, verify=False)
        print r.content

        try:
            if r.status_code == requests.codes.ok:
                # content = r.content.decode('utf-8')
                content = r.content
                jsonObject = json.loads(content)
                print "ok"
                key = jsonObject['Data']['F_Key']
                print key

                return key
            else:
                return ""
        except Exception, e:

            print e
            return ""


