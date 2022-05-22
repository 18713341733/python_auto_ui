from selenium.webdriver.common.by import By


class ExamplePageLocator:
    """
    示例页面的元素定位

    """
    # xpath，通过文案定位
    school = (By.XPATH, "//span[text()='学校']")
    # xpath，通过文案定位
    student = (By.XPATH, "//li[text()='学生']")
    # ID
    searchId = (By.ID, "searchYou")
    # xpath,通过 class
    primaryStudent = (By.XPATH, "//div[@class='ant-primary-student']")
    primaryStudent1 = (By.XPATH, "//button[@class='ant-abc']")
    primaryStudent2 = (By.XPATH, "//span[@class='icon'][1]")
    # 表单
    list1 = (By.XPATH, "//tbody[@class='abc']//tr[@class='bcd'][1]//td[1]")


