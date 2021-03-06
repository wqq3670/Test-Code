from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("吴世勋")
driver.find_element_by_id("su").click()

driver.implicitly_wait(30)
driver.set_window_size(400, 300)
driver.implicitly_wait(10)

#1.浏览器的后退
driver.back()
time.sleep(3)
#2.浏览器的前进
driver.forward()
time.sleep(3)
#3.将浏览器的滚动条拖到浏览器的最底端
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(6)
#4.将浏览器的滚动条拖到浏览器的最顶端
js = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(6)
#5.将滚动条拖到最右端
js = "var q=document.documentElement.scrollLeft=10000"
driver.execute_script(js)
time.sleep(6)
#6.将滚动条拖到最左端
js = "var q=document.documentElement.scrollLeft=0"
driver.execute_script(js)
time.sleep(6)
#7.同时控制浏览器滚动条左右 上下滑动
js = "window.scrollTo(200,100)"
driver.execute_script(js)
time.sleep(3)
driver.quit()
