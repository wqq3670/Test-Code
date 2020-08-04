from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#键盘组合用法
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

time.sleep(6)
driver.find_element_by_id("kw").send_keys("中秋节")
driver.find_element_by_id("su").click()
time.sleep(6)

#1.全选 crtl+a
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
time.sleep(6)

#2.剪贴 crtl+x
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
time.sleep(6)

driver.find_element_by_id("kw").send_keys("国庆节")
driver.find_element_by_id("su").click()
driver.implicitly_wait(10)
driver.find_element_by_link_text("国庆节_百度百科").click()
time.sleep(6)

driver.quit()

