#!/usr/bin/env python3
from selenium import webdriver
from PIL import Image
import time
# Get chromedriver
driver = webdriver.Chrome(executable_path = "/usr/bin/chromedriver")

# Get around lockout
WHAT TO DO HERE?

# Get the page
map_url = "https://www.google.com/maps/place/@51.6527967,-0.0925911,60a,35y,1.03h,52.76t/data=!3m1!1e3!4m5!3m4!1s0x48761f32ec17027d:0x5cd6ebf017bb05ed!8m2!3d51.6534256!4d-0.0924961"
driver.get(map_url)

# Capture and display the screenshot
driver.save_screenshot("ss.png")
screenshot = Image.open("ss.png")
screenshot.show()
