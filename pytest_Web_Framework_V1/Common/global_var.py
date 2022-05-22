# -*- coding:utf-8 -*-



class GlobalVar():
    type = "chrome"
    def set_value(self,value):
        GlobalVar.type = value
    def get_value(self):
        # 获得一个全局变量，不存在则提示读取对应变量失败
        return GlobalVar.type


