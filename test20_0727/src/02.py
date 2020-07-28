from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("吴世勋")
driver.find_element_by_id("su").click()

#1.固定等待
#time.sleep(6)
#2.智能等待
driver.implicitly_wait(30)

driver.maximize_window()
time.sleep(3)
#设置宽和高
driver.set_window_size(400,800)

driver.find_element_by_link_text("吴世勋(韩国歌手、男团EXO成员)_百度百科").click()

time.sleep(3)
driver.quit()
