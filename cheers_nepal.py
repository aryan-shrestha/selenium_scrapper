from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://cheers.com.np/liquor/category?s=na&c=whisky&sc%5B%5D=domestic-whisky&pf=&pt=&p=1&node=child")
print(driver.title)

SCROLL_PAUSE_TIME = 1

# Get Scroll Height
last_height = driver.execute_script("return document.body.scrollHeight")
print(last_height)

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and comapre with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    print("new_height: ", new_height)
    print("last_height: ", last_height)
    if new_height == last_height:
        break
    last_height = new_height

product_list = driver.find_element(By.ID, 'productList')
products = product_list.find_elements(By.CLASS_NAME, "product-list")

for product in products:
    product_name = product.find_element(By.TAG_NAME, "a").find_element(By.TAG_NAME, "h5").text
    product_price = product.find_element(By.TAG_NAME, "h4").text
    print(f"{product_name}: {product_price}")


time.sleep(5)

driver.quit()