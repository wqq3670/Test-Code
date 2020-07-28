from selenium import webdriver
import time

#打印 title 和 url
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

#3.界面最大化
driver.maximize_window()
time.sleep(5)

#4.界面最小化
driver.minimize_window()
time.sleep(5)

#1.打印标题
title = driver.title
print(title)
#2.打印url
url = driver.current_url
print(url)

driver.implicitly_wait(10)
driver.quit()