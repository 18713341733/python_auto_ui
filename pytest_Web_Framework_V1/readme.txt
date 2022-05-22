############################一、运行方式：
一、支持脚本运行方式
1、支持运行所有的case
2、支持运行一个或多个文件下的case
3、支持运行带有标签的case
4、支持运行具体的某一条case


二、总工程执行方式:

python3 runner.py 参数1 参数2 参数3
参数1:
第一个参数 case 执行类型，'all', 'choose', 'tag'，'single'
type = sys.argv[1]

参数2：
第二个参数要执行的文件名称或者标签名称, 多个文件逗号分割
如果第一个参数为tag，则第二个参数为标签名称。
目前只支持四个标签
somke P0 P1 P2 P3,后续可以自己新增


栗子：
执行所有case
sudo python3 runner.py all

执行部分py文件
sudo python3 runner.py choose test_3_lianxi2.py
多个文件逗号隔开
sudo python3 runner.py choose test_3_lianxi2.py,test_2_lianxi1.py

执行带标签的case
sudo python3 runner.py tag P1

执行具体的某条case
需要传文件名、类名和方法名称
sudo python3 runner.py single test_3_mytest3.py TestService test_b_buildserver

执行不同级别的的case
python3 runner.py severity blocker
python3 runner.py severity blocker,critical




其他说明：

pytest.main()：main中传入不同的指令用以执行指定测试用例
-s: 显示程序中的print/logging输出
-v: 丰富信息模式, 输出更详细的用例执行信息
-k：关键字匹配，用and区分：匹配范围（文件名、类名、函数名）
-m: 匹配标签，pytest -m “tag名称”   #运行指定tag名称的用例，也就是运行有@pytest.mark.[标记名]这个标记的case
--steup-show    #完整展示每个用例的fixture调用顺序

https://www.cnblogs.com/jaxon-chen/p/13204745.html
备注：
调试的时候，可以给具体某一条打一个特殊的标签，这样方便调试


############################二、给用例/模块打标签,给用例打级别############################
######给用例打标签
2.1
在pytest.ini文件下，新增标签名称

2.2
在conftest.py文件下，映射刚刚添加的标签
2.3
用例添加标签
@pytest.mark.P0

给测试类加标签
@pytest.mark.P0
class TestClass1(object):

用例同时打两个标签
@pytest.mark.P0
@pytest.mark.P1

参考方法：
https://www.pythonf.cn/read/130621

######给用例分级别
等级介绍
blocker：阻塞缺陷(功能未实现，无法下一步)
critical：严重缺陷(功能点缺失)
normal： 一般缺陷(边界情况，格式错误)
minor：次要缺陷(界面错误与ui需求不符)
trivial： 轻微缺陷(必须项无提示，或者提示不规范)
根据测试用例的重要性划分测试用例等级，如果没指定等级，默认为normal级别

栗子：

    @allure.severity("blocker")
    @allure.story("渠道编号判重")
    def test_j_check_channel_number(self, refresh):
        result = CP(refresh).channel_number()
        assert result == True

参考文件：
https://blog.csdn.net/qq_33801641/article/details/109339371
执行不同级别的的case
python3 runner.py severity blocker
python3 runner.py severity blocker,critical



############################三、注意事项############################
3.1跑自动化时，关掉执行机器的Charles，不然页面可能会报错
3.2确保脚本稳定，尽量加个sleep吧，不然


#################四、多进程###############
参考博客：
https://blog.csdn.net/qq_39208536/article/details/122433899
依赖的是pytest-xdist插件
一、通过main函数运行
2个进程
pytest.main(["-s", "-v", "-m", "cs1", "--html=Outputs/pytest_report/pytest.html", "--alluredir=Outputs/allure_report","-n","2"])
默认自动检查系统cpu个数，然后进行并发
pytest.main(["-s", "-v", "-m", "cs1", "--html=Outputs/pytest_report/pytest.html", "--alluredir=Outputs/allure_report","-n","auto"])

二、通过runner.py运行
在原有命令基础上，追加数字或者追加auto就可以了
目前只支持 all 全部运行和 tag标签多进程
默认是单进程

##################五、失败重试机制#################
参考博客：
https://blog.csdn.net/qq_39208536/article/details/122435367
依赖pytest-rerunfailures 插件
失败包括1、断言失败2、case执行失败（如元素找不到等情况）
一、通过main函数运行
# "--reruns","2" ,失败后再次执行两次
pytest.main(["-s", "-v", "-m", "cs1", "--html=Outputs/pytest_report/pytest.html", "--alluredir=Outputs/allure_report","--reruns","2"])

二、通过runner.py运行
这里默认设置失败后再次执行一次，不支持自定义
目前只支持 all 全部运行和 tag标签多进程

