from selenium.webdriver.common.action_chains import ActionChains
import Navigation
import time

def field(field_no):
    #Navigate to the field page
    link = "https://testx5.kingdoms.com/#/page:resources/location:" + str(field_no) + "/window:building"
    Navigation.driver.get(link)
    #Get Element
    lvl_up = Navigation.driver.find_element_by_xpath('//div[@class="contentHeader"]/span')
    time.sleep(10)
    try:
        status = Navigation.driver.find_element_by_class_name("possible")
    except:
        status = Navigation.driver.find_element_by_class_name("notNow")
    time.sleep(10)
    #Interact with element
    res_status = status.get_attribute("class")
    if "possible" in res_status:
        res_available = True
        lvl_up.click()
        time.sleep(10)
    elif "notNow" in res_status:
        res_available = False
        print("can't build now, not enough resources")
    Navigation.return_main_screen()
    return res_available
    
    

    
def building(building_no):
    #Navigate to the field page
    link = "https://testx5.kingdoms.com/#/page:village/window:welcomeScreen:building/location:" + str(building_no)
    Navigation.driver.get(link)
    time.sleep(4)
    #Get Element
    lvl_up = Navigation.driver.find_element_by_xpath('//div[@class="contentHeader"]/span')
    time.sleep(2)
    #Interact with element
    lvl_up.click()
    #Case 1, enough Resources
    try:
        status = Navigation.driver.find_element_by_class_name("possible")
        res_available = True
        print("Try_click")   
    #Case 2, not enough Resources 
    except:
        status = Navigation.driver.find_element_by_class_name("notNow")
        res_available = False
        print("except_click")
        print("can't build now, not enough resources")
    Navigation.return_main_screen()
    return res_available
    

def check_queue(total_slots):
    #Get Element
    link = "//div[@class='masterBuilderContainer']/div[" + str(total_slots-1) + "]"
    slot = Navigation.driver.find_element_by_xpath(link)
    time.sleep(10)
    #Interact with element
    txt = slot.get_attribute("class")
    print(txt)
    if "empty" in txt:
        q_empty = True
    else:
        q_empty = False
    time.sleep(10)
    return(q_empty)

def check_duration(total_slots):
    #Hovering over the building slot, so that the time window appears
    try:
        link = "//div[@class='masterBuilderContainer']/div[" + str(total_slots-2) + "]"
        slot = Navigation.driver.find_element_by_xpath(link)
        time.sleep(10)
        hover = ActionChains(Navigation.driver).move_to_element(slot)
        hover.perform()
        time.sleep(10)
        #Reading the duration from the time window
        duration = Navigation.driver.find_element_by_xpath("//div[@class='detailsTime']/span")
        time_txt = duration.text
        time_txt = time_txt.split(":",2)[1]
        time.sleep(10)
    except:
        time_txt ="00"
    return time_txt

def inst_complete():
    #Hovering over the building slot, so that the time window appears
    main_slot = Navigation.driver.find_element_by_class_name("constructionContainer")
    time.sleep(4)
    hover = ActionChains(Navigation.driver).move_to_element(main_slot)
    hover.perform()
    time.sleep(2)
    #Reading the duration from the time window
    #inst_button = Navigation.driver.find_element_by_class_name("content")
    inst_button = Navigation.driver.find_element_by_xpath("//button[@class='free']/div")
    time.sleep(2)
    Navigation.driver.execute_script("arguments[0].click();", inst_button)
    #inst_button.click()
    #try:
        
    #except:
    #    print("No Building to skip")
