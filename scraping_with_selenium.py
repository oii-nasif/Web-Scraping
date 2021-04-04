from selenium import webdriver

PATH = '/home/hbins413/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://nasif.tech")
print(driver.title)
driver.quit()