# coding:utf-8
# from Tkinter import *
import tkSimpleDialog
import tkMessageBox
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from Tkinter import *  # 导入 Tkinter 库
from http import Http
from chrome import Chrome

root = Tk(screenName="dialog")  # 创建窗口对象的背景色
root.geometry("200x100+960+500")
L_titile = Label(root, pady=5, text='请输入验证码')
L_titile.pack()

e = Entry(root)
e.pack(padx=5)


def show_tip():
    tkMessageBox.showwarning("提示", "验证码不能为空\n")


def show_code_error():
    tkMessageBox.showwarning("提示", "验证码不正确，请重新输入\n")

def close():
    tkMessageBox.showwarning("提示", "关闭所有界面")

def log():
    print e.get()
    number = e.get()
    if number == '':
        show_tip()
    else:
        key = Http.get_key(number)
        print key

        if key == '':
            show_code_error()
        else:
            print key

            root.withdraw()
            chrome = Chrome(key)
            chrome.open_web()

            # root.withdraw()
            # close()
            #
            # root.destroy()





B_1 = Button(root, text="确定", pady=5, padx=20, command=log)
B_1.pack(pady=10)

root.mainloop()  # 进入消息循环
