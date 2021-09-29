#!/usr/bin/env python3
import pyautogui
from PIL import Image
import os
import csv
import time

# SEE : https://pyautogui.readthedocs.io/en/latest/

# Let's clear things out just to be tidy
for filename in os.listdir("Pics"):
  file_path = os.path.join("Pics", filename)
  os.remove(file_path)

for filename in os.listdir("Animations"):
  file_path = os.path.join("Animations", filename)
  os.remove(file_path)

# Doing the do
with open('building-data.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  for row in csv_reader:
    # Do NORTH
    pyautogui.click(300, 80)    
    north_location = "https://www.google.com/maps/place/@" + row[1] + "," + row[2] + ",60a,35y,1.03h,52.76t/data=!3m1!1e3!4m5!3m4!1s0x48761f32ec17027d:0x5cd6ebf017bb05ed!8m2!3d51.6534256!4d-0.0924961\n"
    north_filename = "Pics/" + row[0] + "_NORTH.png"
    pyautogui.write(north_location)
    time.sleep(10)
    if os.path.exists(north_filename):
      os.remove(north_filename)
    pyautogui.screenshot(north_filename, region=(550,250, 1250, 850))

    # Do EAST
    pyautogui.click(300, 80)    
    east_location = "https://www.google.com/maps/place/@" + row[1] + "," + row[2] + ",60a,35y,90h,52.76t/data=!3m1!1e3!4m5!3m4!1s0x48761f32ec17027d:0x5cd6ebf017bb05ed!8m2!3d51.6534256!4d-0.0924961\n"
    east_filename = "Pics/" + row[0] + "_EAST.png"
    pyautogui.write(east_location)
    time.sleep(10)
    if os.path.exists(east_filename):
      os.remove(east_filename)
    pyautogui.screenshot(east_filename, region=(550,250, 1250, 850))
    
    # Make the animated gifs
    images = []
    for file in os.listdir("Pics"):
      if file.startswith(row[0]): 
        images.append(Image.open("Pics/" + file))
    images[0].save("Animations/" + row[0] + "_ANIM.gif", save_all=True, append_images = images[1:], optimize = True, duration = 3000, loop = 0)
    images.clear()


