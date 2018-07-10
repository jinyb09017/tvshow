# coding:utf-8
from http import Http
from chrome import Chrome

key = Http.get_key_new()
print key

if key == '':
    print "验证码错误"
else:
    print key

chrome = Chrome(key)
chrome.open_web_up()
input ("wait....")
