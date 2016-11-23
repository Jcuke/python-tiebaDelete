# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os

sleepTime = 0.3
profile_dir = r"C:\Users\wangjinwen.NETFINWORKS\AppData\Local\Google\Chrome\User Data"  # 对应你的chrome的用户数据存放路径
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=" + os.path.abspath(profile_dir))

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://tieba.baidu.com/i/22440130/concern")
cookie= driver.get_cookies()
print(cookie)
print(driver.title)
now_handle = driver.current_window_handle #获取当前窗口句柄
while True:
    time.sleep(0.8)
    page = driver.find_element_by_class_name("btn_unfollow")
    print page
    if page:
        page.click()
        time.sleep(sleepTime)
        print(driver.title)
        js = "$('.dialogJanswers').children('input')[0].click()"
        driver.execute_script(js)
        time.sleep(sleepTime)
    else:
        break


# driver.quit()