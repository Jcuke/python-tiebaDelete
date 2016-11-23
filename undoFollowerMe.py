# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os

sleepTime = 0.4
profile_dir = r"C:\Users\wangjinwen.NETFINWORKS\AppData\Local\Google\Chrome\User Data"  # 对应你的chrome的用户数据存放路径
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=" + os.path.abspath(profile_dir))

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://tieba.baidu.com/i/22440130/fans")
cookie= driver.get_cookies()
print(cookie)
print(driver.title)
now_handle = driver.current_window_handle #获取当前窗口句柄
time.sleep(3)
while True:
    time.sleep(0.5)
    js = "$(\"div[id*='add_blacklist_']\").show()"
    driver.execute_script(js)
    time.sleep(sleepTime)

    page = driver.find_element_by_id("add_blacklist_btn")
    print page
    if page:
        page.click()
        time.sleep(sleepTime)

        js = "$('.dialogJanswers').children('input')[0].click()"
        driver.execute_script(js)
        time.sleep(sleepTime)

    else:
        break


# driver.quit()