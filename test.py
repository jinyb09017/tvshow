#coding=utf-8
import requests

cs_url = 'https://cola.apitops.com/api/version/getlatest'
# cs_url = 'http://localhost:13145/api/version/getlatest'

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
r = requests.post(cs_url, data=datas, headers=mHeader, verify=False)

print r.status_code