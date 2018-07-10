# coding:utf-8
import Tkinter
import tkSimpleDialog
#
# root = Tkinter.Tk()
# root.withdraw()
# var = tkSimpleDialog.askstring("Dialog", "请输入验证码")
# print var
# from Tkinter import *
#
# class MyDialog:
#
#     def __init__(self, parent):
#
#         top = self.top = Toplevel(parent)
#
#         Label(top, text="Value").pack()
#
#         self.e = Entry(top)
#         self.e.pack(padx=5)
#
#         b = Button(top, text="OK", command=self.ok)
#         b.pack(pady=5)
#
#     def ok(self):
#
#         print "value is", self.e.get()
#
#         self.top.destroy()
#
#
# root = Tk()
# root.withdraw()
# Button(root, text="Hello!").pack()
# root.update()
#
# d = MyDialog(root)
#
# root.wait_window(d.top)


from Tkinter import *

class MyDialog:
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Value").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)

        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

        c = Button(top, text="cancel", command=self.ok)
        c.pack(pady=5)

    def ok(self):

        print "value is", self.e.get()

        self.top.destroy()


root = Tk()
# root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
root.withdraw()
d = MyDialog(root)

root.wait_window(d.top)

