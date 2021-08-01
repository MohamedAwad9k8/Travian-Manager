import SeleniumSetting
import time
from selenium.webdriver.common.keys import Keys
driver = SeleniumSetting.start()

#Open Main Screen
def open_main_screen():
    
    driver.get("https://testx5.kingdoms.com/#/page:village")
    time.sleep(10)

#Return to WelcomeScreen
def return_main_screen():
    driver.get("https://testx5.kingdoms.com/#/page:village")
    time.sleep(2)

#Close Connection
def close_connection():
    driver.quit()
    driver.close()
