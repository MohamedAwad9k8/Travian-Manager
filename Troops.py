import Navigation
from selenium.webdriver.common.keys import Keys
import time

def infantry_train(type, number):
    #Navigate to Barracks
    Navigation.driver.get("https://testx5.kingdoms.com/#/page:village/window:welcomeScreen:building/location:29")

    #Get Elements
    type1 = Navigation.driver.find_element_by_class_name("unitType1")
    type2 = Navigation.driver.find_element_by_class_name("unitType2")
    numberofSoliders = Navigation.driver.find_element_by_xpath('//div[@class="inputContainer"]/input')
    submit = Navigation.driver.find_element_by_class_name("footerButton")

    #Interact with Elements
    if (type == "phalanx"):
        type1.click()
    elif (type == "swordsman"):
        type2.click()
    time.sleep(2)
    numberofSoliders.clear()
    time.sleep(1)
    numberofSoliders.send_keys(str(number),Keys.ENTER)
    time.sleep(1)
    submit.click()
    time.sleep(2)