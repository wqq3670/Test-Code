from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
time.sleep(3)

#10.text的使用
t = driver.find_element_by_css_selector("#s-bottom-layer-right").text
print(t)

#9.clear submit text的使用
#driver.find_element_by_css_selector("#kw").send_keys("1314")
#driver.find_element_by_css_selector("#su").click()
#time.sleep(8)
#driver.find_element_by_css_selector("#kw").clear()
#driver.find_element_by_css_selector("#kw").send_keys("521")
#driver.find_element_by_css_selector("#su").submit()
#time.sleep(8)

#8.通过css selector定位
#driver.find_element_by_css_selector("#kw").send_keys("1314")
#driver.find_element_by_css_selector("#su").click()

#7.通过xpath定位(一定可以定位到)
#driver.find_element_by_xpath("//*[@id='kw']").send_keys("王振鹏")
#driver.find_element_by_xpath("//*[@id='su']").click()

#6.通过tag name定位
#driver.find_element_by_tag_name("input").send_keys("521")
#失败，因为input太多了，不唯一

#5.通过partial link text定位
#driver.find_element_by_partial_link_text("加油").click()

#4.通过link text定位
#driver.find_element_by_link_text("高考加油").click()

#3.通过class name定位
#driver.find_element_by_class_name("s_ipt").send_keys("高考成绩")
#报错的原因是 class name中属性有两个，若要用class name定位元素时，
#这个class name的属性当且仅当只有一个,一旦属性大于一个便不能用class name定位
#driver.find_element_by_class_name("bg s_btn").click()

#2.通过name定位
#driver.find_element_by_name("wd").send_keys("0412")
#driver.find_element_by_id("su").click()

#1.通过id定位
#driver.find_element_by_id("kw").send_keys("吴世勋")
#driver.find_element_by_id("su").click()

time.sleep(8)
driver.quit()