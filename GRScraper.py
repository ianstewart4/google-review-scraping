from selenium import webdriver

PATH = "/Users/ianstewart/Desktop/Python/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://play.google.com/store/apps/details?id=com.episodeinteractive.android.catalog&hl=en&gl=US")
driver.quit()
