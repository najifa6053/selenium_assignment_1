import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager    


def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver
#

#Using ID
def test_id(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    driver.quit()
    
    
#Using NAME
def test_name(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.NAME, "login-button").click()
    time.sleep(2)
    driver.quit()
    
    
#Using CLASS NAME
def test_class_name(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "input_error form_input").send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "input_error form_input").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "submit-button btn_action").click()
    time.sleep(2)
    driver.quit()
    
#Using TAG NAME
def test_tag_name(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.TAG_NAME, "input").send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.TAG_NAME, "input").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.TAG_NAME, "input").click()
    time.sleep(2)
    driver.quit()
    
#Using XPATH Id
def test_xpath_id(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@id="login-button"]').click()
    time.sleep(2)
    driver.quit()
    
#Using XPATH Name
def test_xpath_name(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@name="user-name"]').send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@name="login-button"]').click()
    time.sleep(2)
    driver.quit()
    
    
#Using XPATH Class Name
def test_xpath_class_name(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@class="input_error form_input"]').send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@class="input_error form_input"]').send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@class="submit-button btn_action"]').click()
    time.sleep(2)
    driver.quit()
    
if __name__ == "__main__":
    driver = setup_driver()
    #test_id(driver)
    #test_name(driver)
    #test_class_name(driver)
    #test_tag_name(driver)
    #test_xpath_id(driver)
    #test_xpath_name(driver)
    test_xpath_class_name(driver)