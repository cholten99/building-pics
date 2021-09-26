#!/usr/bin/env python3
from selenium import webdriver
from PIL import Image
import time
# Get chromedriver
driver = webdriver.Chrome(executable_path = "/usr/bin/chromedriver")

# Get around lockout

# Get the page
map_url = "https://www.google.com/maps/place/@51.6527967,-0.0925911,60a,35y,1.03h,52.76t/data=!3m1!1e3!4m5!3m4!1s0x48761f32ec17027d:0x5cd6ebf017bb05ed!8m2!3d51.6534256!4d-0.0924961"

# Hackity hack
driver.get("https://medium.com/")
driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/div/div/div/div[3]/span[4]/div/div/p/span/a').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div/div/div/div/div[3]/div[1]/a').click()
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys("cholten99@gmail.com")
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()


# driver.get(map_url)

# Capture and display the screenshot

#driver.save_screenshot("ss.png")
#screenshot = Image.open("ss.png")
#screenshot.show()

