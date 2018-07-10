# coding:utf-8
# from Tkinter import *
import tkSimpleDialog
import tkMessageBox
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from Tkinter import *  # 导入 Tkinter 库
from http import Http
root = Tk(screenName="dialog")  # 创建窗口对象的背景色
root.geometry("200x100+960+500")
L_titile = Label(root, pady=5, text='请输入验证码')
L_titile.pack()

e = Entry(root)
e.pack(padx=5)


def show_tip():
    tkMessageBox.showwarning("提示", "验证码不能为空\n")


def log():
    print e.get()
    number = e.get()
    if number == '':
        show_tip()
    else:
        request_key()
        root.destroy()


def request_key():
    payload = {"code": "486660"}
    cs_url = 'https://tv.apitops.com/newtv/ValidateCode'
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    r = requests.post(cs_url, data=payload, cert='xiaoguan.crt')
    print r.content
    if r.status_code == requests.codes.ok:
        print "ok"
    else:
        print "bad"


B_1 = Button(root, text="确定", pady=5, padx=20, command=log)
B_1.pack(pady=10)

root.mainloop()  # 进入消息循环
