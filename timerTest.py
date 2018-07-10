# coding=utf-8

# 用于定时检测app网站的情况
# coding:utf-8
import requests
import json
# http://gateway.test.apitops.com/apibuild/Profile/GetAdminInfoV1?sign=b600712f94fa1b2eda7bfdbd67709011 HTTP/1.1
import smtplib
import threading
from email.mime.text import MIMEText
import time

# cs_url = 'https://cola.apitops.com/api/version/getlatest'
# cs_url = 'localhost:13145/app/listChannel/21'
cs_url = 'http://cola.test.apitops.com/api/version/getlatest'

mHeader = {
    'source': 'app',
    'agent': 'android',
    'time': '20151314',
    'random': '1',
    'sign': '72ac88381d50e4725ff72cab5c9acc45'

}
datas = {
    'VersionNumber': '3.1.2',
    'ChannelCode': 'debug',
    'AppKey': 'f31ebace30134828a37e1a062bcfbb74',
    'AppCatalog': '2',
    'AddVer': '0'
}


def requestTest():
    try:
        start = time.time()
        print 'start'
        r = requests.post(cs_url, data=datas, headers=mHeader)
        print 'end'
        end = time.time()

        total = int(end - start)

        print total

        print r.status_code

        if r.status_code == 200:
            content = r.content.decode('utf-8')
            print content

            result = json.loads(content)

            print content

            if result['code'] == 200 or result['code'] == 100:
                print '成功'
            else:
                print '失败'

        else:
            print "失败"

    except requests.exceptions.RequestException, error:
        print error



# 一个小时请求一次
timeGap = 1 * 60 * 10
retry = 0


def timeRequest():
    while 1 == 1:
        requestTest();


timeRequest()
