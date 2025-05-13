from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime

import time
import requests
import os

# Set up Chrome WebDriver
service = Service(executable_path=r"C:\Users\rathi\OneDrive\Documents\learning\Python\chromedriver.exe")  # Replace with your chromedriver path
driver = webdriver.Chrome(service=service)

# Get today's date in ddmmyyyy format
today = datetime.now().strftime("%d%m%Y")
image_name = f"{today}.jpg"
print ("image_name:",image_name)
 
# Construct the image URL
base_url = "https://www.tamildailycalendar.com/2025/"
driver.get(base_url)
time.sleep(5)

image_url = base_url + image_name

file_name = driver.find_element(By.PARTIAL_LINK_TEXT, image_name)
print ("line 26",file_name)
file_name.click()

# Visit the image URL directly




# Wait for the image to load
time.sleep(2)

# Use requests to download and save image
response = requests.get(image_url)

try:
    img_element = driver.find_element(By.TAG_NAME, "img")
    img_src = img_element.get_attribute("src")
    print("Image source found:", img_src)

    # Now download using requests
    img_data = requests.get(img_src).content
    with open(image_name, 'wb') as f:
        f.write(img_data)
    print("Image saved as", image_name)
except Exception as e:
    print("Could not find image:", str(e))
driver.quit()




