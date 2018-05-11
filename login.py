from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://192.168.100.100:8090')

username = driver.find_element_by_id("username")
password = driver.find_element_by_name("password")

username.send_keys("USERNAME_GOES_HERE")
password.send_keys("PASSWORD_GOES_HERE")

a = driver.execute_script("javascript:submitRequest()")