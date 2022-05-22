# -*- coding:utf-8 -*-
# 创建者： 喵酱
# 功能点：百度搜索页面


import os, pytest, allure

from PageObjects.step_baidu_serach import BaiduPage as BD

root = os.path.dirname(os.path.abspath(__file__))

@allure.feature("模块：百度搜索")
class TestChannel:

    @pytest.mark.P3
    @allure.story("搜索搜狗")
    def test_search_sougou(self, refresh):
        """
        操作：搜索搜狗
        断言：结果列表展示搜狗
        """
        result_text = BD(refresh).search_sougou()
        assert result_text == '搜狗'

    @pytest.mark.P1
    @allure.story("搜索淘宝")
    def test_search_taobao(self, refresh):
        """
        操作：搜索淘宝
        断言：结果列表展示淘宝
        """
        result_text = BD(refresh).search_taobao()
        assert result_text == '淘宝'

