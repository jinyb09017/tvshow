#coding:utf-8
import requests
# http://gateway.test.apitops.com/apibuild/Profile/GetAdminInfoV1?sign=b600712f94fa1b2eda7bfdbd67709011 HTTP/1.1

cs_url = 'http://gateway.test.apitops.com/apibuild/Profile/GetAdminInfoV1'

mHeader = {
    'Authorization': '453fae30-53ae-11e6-a8b3-288023a0ea0c',
    'Gateway-Version': '1',
    'Date': 'Mon, 25 Jul 2016 08:45:35 GMT+0800',
    'Consumer-Key': 'ae80b757c66741ccace3169a0d223acd',
    'User-Agent': 'com.kakao.topbroker/4.1.0-debug Dalvik/1.6.0 (Linux; U; Android 4.4.4; R8107 Build/KTU84P)',
    'Disable-Function': 'Cookie'
}
param = {
    'brokerKid': '33036',
    'sign': '6fbae0c3e653b6eee2068d2f9741e140'
}
datas = {
    'ak': '453fae30-53ae-11e6-a8b3-288023a0ea0c',
    'app': 'app_broker',
    'time': '20160725094535420',
    'agent': 'android'
}


def getQuery(mHeader):
    queryStr = ''
    for key in mHeader.keys():
        print key, mHeader[key]
        queryStr += '&' + key + '=' + mHeader[key]
    # print queryStr

    if len(queryStr) > 1:
        queryStr = queryStr[1:]
    print queryStr

    return queryStr


def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()


# print getQuery(mHeader)
md5Value = md5(getQuery(datas))

md5last = 'gateway.test.apitops.com/apibuild/Profile/GetAdminInfoV1'.lower() + md5Value + mHeader[
    'Date'] + '374fa3ab6b1fae595db5382afe415bce'
mHeader['Signature'] = 'v3:'+md5(md5last)
# mHeader['Signature'] = 'af8433645e505da7b5a554a5bcf55aea'

# print md5(getQuery(mHeader))

print mHeader
#
# r = requests.post(cs_url, params=param, data=datas)
r = requests.post(cs_url, params=param, headers=mHeader, data=datas)
# # print r.url
#
print r.content.decode('utf-8')
