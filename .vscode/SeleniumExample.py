
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://google.com')

element = driver.find_element_by_name('q')

element.send_keys("test")

element.send_keys(Keys.RETURN)

driver.quit()

print("yep")
