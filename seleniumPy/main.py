from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # Allows us to send a key

# wait for the presence of elements to avoid accessing something that doesn't exist
# so wait for the presence of an element before going forward
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

## setup headless mode
## instantiate a Chrome options object
options = webdriver.ChromeOptions()

# set the options to use Chrome in headless mode
options.add_argument("--headless=new")

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)

driver.get('https://google.com')

# implementation for waiting for the presence of elements
# this is going to use our webdriver, it is going to wait for up to 5 seconds until we
# locate and element with that class name
WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
) # pass in driver an number of seconds we want to have as a timeout


input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
# input_element.clear() # is handy if the input field is already populated. So it clears what is there

# send keys, types something to input the element
input_element.send_keys('specialized chisel comp' + Keys.ENTER)

# Find and click on a link
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Chisel Hardtail Comp")
link.click()

time.sleep(10)

driver.quit()