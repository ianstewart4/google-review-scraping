from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/ianstewart/Desktop/Python/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://play.google.com/store/apps/details?id=com.episodeinteractive.android.catalog&hl=en&gl=US")


search = driver.find_elements_by_class_name("")

time.sleep(5)

driver.quit()