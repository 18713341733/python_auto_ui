import time
import re
from PageLocators.baidu_page_locator import BaiduPageLocator as BD
from Common.basepage import BasePage


class BaiduPage(BasePage):

    def search_sougou(self):
        self.input_text(BD.searchValue,"搜狗",doc="输入框输入搜狗")
        self.click(BD.searchBtn, doc="点击搜索按钮")
        text_search = self.get_element_text(BD.list_name, doc="搜索结果列表的第一条数据")
        return text_search

    def search_taobao(self):
        self.input_text(BD.searchValue, "淘宝", doc="输入框输入搜狗")
        self.click(BD.searchBtn, doc="点击搜索按钮")
        text_search = self.get_element_text(BD.list_name, doc="搜索结果列表的第一条数据")
        return text_search


