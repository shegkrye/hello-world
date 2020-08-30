from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
       
    browser.get(link)
    
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.execute_script("window.scrollBy(0, 100);")
    button = browser.find_element_by_xpath("//button[contains(text(),'Book')]")
    button.click()
    input5 = browser.find_element_by_xpath("//span[@id='input_value']")
    x=input5.text
    y=calc(x)
    input4 = browser.find_element_by_xpath("//input[@id='answer']")
    input4.send_keys(y)
    input2 = browser.find_element_by_xpath("//button[@type='submit']")
    input2.click()
    
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    
    time.sleep(10)
    
    browser.quit()