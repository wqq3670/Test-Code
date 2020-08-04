from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

#鼠标事件
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.implicitly_wait(10)

driver.find_element_by_id("kw").send_keys("乃万")
#1.右击鼠标
su1 = driver.find_element_by_id("su")
ActionChains(driver).context_click(su1).perform()
time.sleep(3)
#2.双击鼠标
ActionChains(driver).double_click(su1).perform()
time.sleep(3)
#3.拖动
#定义元素的原位置
element = driver.find_element_by_link_text("乃万_百度百科")
#定义元素要拖动到的位置
target = driver.find_element_by_id("su")
ActionChains(driver).drag_and_drop(element, target).perform()

#4.移动（悬停）
ActionChains(driver).move_to_element(element).perform()
#通过click 操作来识别 move_to_element 操作是否完成
#ActionChains(driver).move_to_element(element).click().perform()

time.sleep(2)
driver.quit()
