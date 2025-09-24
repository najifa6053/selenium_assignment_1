import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver import ActionChains as AC



def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver


def fill_text_inputs(driver):
    driver.get("https://demoqa.com/text-box")
    name_text = driver.find_element(By.ID, "userName").send_keys("Najifa Alam Esha")
    time.sleep(1)
    email_text = driver.find_element(By.ID, "userEmail").send_keys("najifa@example.com")
    time.sleep(1)
    current_address = driver.find_element(By.ID, "currentAddress").send_keys("Dhaka, Bangladesh")
    permanent_address = driver.find_element(By.ID, "permanentAddress").send_keys("Dhaka, Bangladesh")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    output_name = driver.find_element(By.ID, "name")
    assert "Najifa Alam Esha" in output_name.text
    print("Text input test passed.")

def radio_button_test(driver):
    driver.get("https://demoqa.com/radio-button")
    yes_radio = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    yes_radio.click()
    time.sleep(1)
    impressive_radio = driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
    impressive_radio.click()
    time.sleep(1)
    no_radio = driver.find_element(By.XPATH, "//label[@for='noRadio']")
    no_radio.click() 
    time.sleep(1)

    output_yes = driver.find_element(By.XPATH, "//span[@class='text-success']")
    assert "Impressive" in output_yes.text


def checkbox_test(driver):
    driver.get("https://demoqa.com/checkbox")
    expand_button = driver.find_element(By.XPATH, "//button[@title='Expand all']")
    expand_button.click()
    time.sleep(1)
    desktop_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-desktop']")
    desktop_checkbox.click()
    time.sleep(1)
    documents_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-documents']")
    documents_checkbox.click()  
    time.sleep(1)
    downloads_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-downloads']")
    downloads_checkbox.click()
    time.sleep(1)
    output = driver.find_element(By.ID, "result")
    assert "desktop" in output.text   
    print("All tests completed successfully.")


def button_test(driver):
    driver.get("https://demoqa.com/buttons")
    double_click_button = driver.find_element(By.ID, "doubleClickBtn")
    AC(driver).double_click(double_click_button).perform()
    time.sleep(1)
    right_click_button = driver.find_element(By.ID, "rightClickBtn")
    AC(driver).context_click(right_click_button).perform()
    time.sleep(1)
    dynamic_click_button = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    dynamic_click_button.click()
    time.sleep(1)

    output_double = driver.find_element(By.ID, "doubleClickMessage")
    assert "You have done a double click" in output_double.text
    output_right = driver.find_element(By.ID, "rightClickMessage")
    assert "You have done a right click" in output_right.text
    output_dynamic = driver.find_element(By.ID, "dynamicClickMessage")
    assert "You have done a dynamic click" in output_dynamic.text
    
    
def hover_test(driver):
    driver.get("https://demoqa.com/menu")
    time.sleep(1)
    main_item2 = driver.find_element(By.XPATH, "//a[text()='Main Item 2']")
    AC(driver).move_to_element(main_item2).perform()
    time.sleep(1)
    sub_item2 = driver.find_element(By.XPATH, "//a[text()='SUB SUB LIST » Sub Sub Item 1']")
    AC(driver).move_to_element(sub_item2).perform()
    time.sleep(1)
    sub_sub_item1 = driver.find_element(By.XPATH, "//a[text()='Sub Sub Item 1']")
    sub_sub_item1.click()
    time.sleep(1)
    print("Hover test completed successfully.")
    
    
def file_upload_test(driver):
    driver.get("https://demoqa.com/upload-download")
    upload_input = driver.find_element(By.ID, "uploadFile")
    upload_input.send_keys("ASSIGNMENT_1\README.mdt")  # Change to a valid file path
    time.sleep(1)
    uploaded_file_path = driver.find_element(By.ID, "uploadedFilePath")
    assert "file.txt" in uploaded_file_path.text
    print("File upload test passed.")


def alert_test(driver):
    driver.get("https://demoqa.com/alerts")
    alert_button = driver.find_element(By.ID, "alertButton")
    alert_button.click()
    time.sleep(1)
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(1)
    alert_button_5s = driver.find_element(By.ID, "timerAlertButton")
    alert_button_5s.click()
    time.sleep(6)
    alert_5s = driver.switch_to.alert
    alert_5s.accept()
    time.sleep(1)
    alert_confirm_button = driver.find_element(By.ID, "confirmButton")
    alert_confirm_button.click()
    time.sleep(1)
    alert_confirm = driver.switch_to.alert
    alert_confirm.dismiss()
    time.sleep(1)
    alert_prompt = driver.find_element(By.ID, "promtButton")
    alert_prompt.click()
    time.sleep(1)
    alert_prompt = driver.switch_to.alert
    alert_prompt.send_keys("Cancel")
    alert_prompt.dismiss()
    time.sleep(1)
    output_text = driver.find_element(By.ID, "promptResult")
    assert "Cancel" in output_text.text
    assert "Cancel" in alert_prompt.text
    print("Alert test completed successfully.")
    
    
def time_test(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    time.sleep(6)
    color_change_button = driver.find_element(By.ID, "colorChange")
    assert "rgb(220, 53, 69)" in color_change_button.value_of_css_property("color")
    print("Time test completed successfully.")
    
    
def web_driver_wait_test(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    driver.implicitly_wait(5)
    visible_after_button = driver.find_element(By.ID, "visibleAfter")
    assert visible_after_button.is_displayed()
    print("WebDriver wait test completed successfully.")


def button_enabled_disabled_test(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    enabled_button = driver.find_element(By.ID, "enableAfter")
    assert enabled_button.is_enabled()
    print("Button enabled/disabled test completed successfully.")
    
    
def screenshot_test(driver):
    driver.get("https://demoqa.com/")
    driver.save_screenshot("screenshot.png")
    print("Screenshot taken successfully.")
    
    
def modal_all_test(driver):
    driver.get("https://demoqa.com/modal-dialogs")
    small_modal_button = driver.find_element(By.ID, "showSmallModal")
    small_modal_button.click()
    time.sleep(1)
    close_small_modal = driver.find_element(By.ID, "closeSmallModal")
    close_small_modal.click()
    time.sleep(1)
    large_modal_button = driver.find_element(By.ID, "showLargeModal")
    large_modal_button.click()
    time.sleep(1)
    close_large_modal = driver.find_element(By.ID, "closeLargeModal")
    close_large_modal.click()
    time.sleep(1)
    print("Modal dialog test completed successfully.")

if __name__ == "__main__":
    driver = setup_driver()
    #fill_text_inputs(driver)
    #radio_button_test(driver)
    #checkbox_test(driver)
    #button_test(driver)
    #hover_test(driver)
    #file_upload_test(driver)
    #alert_test(driver)
    #time_test(driver)
    #web_driver_wait_test(driver)
    #button_enabled_disabled_test(driver)
    #screenshot_test(driver)
    modal_all_test(driver)