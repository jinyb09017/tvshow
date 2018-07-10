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
cs_url = 'http://cola.test.apitops.com/api/version/getlatest'
# cs_url = 'http://cola.test.apitops.com/api/version/getlatest'

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

sendMsgTotal = 0


# 发送邮件
def sendEmail(msg):
    global sendMsgTotal
    sendMsgTotal = sendMsgTotal + 1

    _user = "407007276@qq.com"  # 用户名
    _pwd = "wqdfnziircgybiei"  # 口令
    _to = "407007276@qq.com"

    msg = MIMEText(msg)
    msg["Subject"] = "nodejs服务器通知邮件"
    msg["From"] = _user
    msg["To"] = _to

    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(_user, _pwd)
        s.sendmail(_user, _to, msg.as_string())
        s.quit()
        print "send email : " + str(sendMsgTotal)
    except smtplib.SMTPException, e:
        print "Falied,%s" % e


# 发起网络请求


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

            result = json.loads(content)

            print result

            if result['code'] == 200 or result['code'] == 100:
                print '成功'
            else:
                print '失败'
                sendEmail(r.content)
        else:
            print "失败"
            sendEmail(r.content)
    except requests.exceptions.RequestException, error:
        print error
        sendEmail(str(error))


# 一个小时请求一次
timeGap = 1 * 60 * 10
retry = 0


def timeRequest():
    global retry
    retry = retry + 1
    # print retry
    print 'send request :' + str(retry)
    requestTest()
    global t  # Notice: use global variable!
    t = threading.Timer(timeGap, timeRequest)
    if sendMsgTotal < 3:
        t.start()
    else:
        t.cancel()


timeRequest()
