# coding:utf-8
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail(self):
        print self.name
        print self.age

    @staticmethod
    def static_method():
        print("是静态方法")

    @classmethod
    def class_method(cls):
        print("是类方法")


obj1 = Person('wupeiqi', 18)
print obj1.name  # 直接调用obj1对象的name属性
print obj1.age  # 直接调用obj1对象的age属性

obj2 = Person('alex', 73)
print obj2.name  # 直接调用obj2对象的name属性
print obj2.age  # 直接调用obj2对象的age属性

obj1.detail()
