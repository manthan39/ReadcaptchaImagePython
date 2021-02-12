from PIL import Image
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
from io import BytesIO

driver = webdriver.Chrome('C:/Users/Lenovo/Desktop/chromedriver.exe')
driver.maximize_window()
driver.get("https://services.ecourts.gov.in/ecourtindia_v4_bilingual/cases/qs_civil_advocate.php?state=D&state_cd=17&dist_cd=13#") 

element = driver.find_element_by_id("captcha_image")
location = element.location
size = element.size

driver.save_screenshot("image.png")

x = location['x']
y = location['y']
width = location['x']+size['width']
height = location['y']+size['height']

im = Image.open('image.png')
im = im.crop((int(x), int(y), int(width), int(height)))
im.save('image.png')

payload = {'apikey':"32062d643f88957", "OCREngine": 2}
f_path = "C:/Users/Lenovo/Desktop/image.png"
with open(f_path, 'rb') as f:
    j = requests.post('https://api.ocr.space/parse/image', files={f_path: f}, data=payload).json()
    if j['ParsedResults']:
        print(j['ParsedResults'][0]['ParsedText'])
        captcha = (j['ParsedResults'][0]['ParsedText'])
        # 8620


inputElement = driver.find_element_by_name("captcha")
inputElement.send_keys(captcha)
