def start():
    from selenium import webdriver
    PATH = "D:\Courses\python\Python Projects\Travian Manager\Chrome Driver\chromedriver.exe"
    options = webdriver.ChromeOptions() 
    options.add_argument("user-data-dir=C:\\Users\\moham\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1") #Path to your chrome profile
    options.add_argument("--start-maximized")
    options.headless = False
    driver = webdriver.Chrome(executable_path=PATH ,options = options)
    return driver