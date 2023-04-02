from selenium import webdriver
import time


url = "https://github.com/Greekz" #Change to your GitHub link profile


driver = webdriver.Chrome()


driver.get(url)


refresh_interval = 1


while True:

    time.sleep(refresh_interval)


    driver.refresh()