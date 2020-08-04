from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#打开禅道并登录
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:82/index.php")
driver.implicitly_wait(30)

#1.点击开源版
driver.find_element_by_id("zentao").click()

#2.输入用户名，密码
driver.find_element_by_id("account").send_keys("admin")
#调用按键Tab来从用户名跳转到密码框（但仅仅只是一个跳转作用）
driver.find_element_by_id("account").send_keys(Keys.TAB)
time.sleep(5)
#真正要输密码还需要定位到密码这个元素进行
driver.find_element_by_name("password").send_keys("15229873670exo")

#3.登录
#通过输完密码（定位密码框）利用ENTER键登录
#driver.find_element_by_name("password").send_keys(Keys.ENTER)
#通过定位到登录按钮 利用ENTER键登录
driver.find_element_by_id("submit").send_keys(Keys.ENTER)
#通过定位到登录按钮 利用click()登录
#driver.find_element_by_id("submit").click()

time.sleep(5)
driver.quit()

