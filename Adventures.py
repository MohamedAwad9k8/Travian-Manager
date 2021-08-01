import Navigation
import time

def send(duration):
    #Navigate to Adventures
    adventure_button = Navigation.driver.find_element_by_class_name("adventureLink")
    adventure_button.click()

    #Get Elements
    short_adventure = Navigation.driver.find_element_by_class_name("adventure_short_large_illu") 
    long_adventure = Navigation.driver.find_element_by_class_name("adventure_long_large_illu")
    submit = Navigation.driver.find_element_by_xpath('//div[@class="buttonWrapper"]/button')

    #Interact with Elements
    if (duration == "long"):
        long_adventure.click()
    elif (duration == "short"):
        short_adventure.click()
    time.sleep(2)
    submit.click()
    time.sleep(2)
