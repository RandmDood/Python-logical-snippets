from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

trend_bot = webdriver.Chrome()
trend_bot.get("https://trends.google.com/trends/")
trend_bot.find_element(by=By.XPATH, value='//*[@id="gb"]/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/button').click()

trend_bot.implicitly_wait(5)
trend_page = trend_bot.current_window_handle
trend_bot.switch_to.window(trend_page)

trends = trend_bot.find_elements(by=By.CSS_SELECTOR, value=".title span a")
search_count = trend_bot.find_elements(by=By.CLASS_NAME, value="search-count-title")
source = trend_bot.find_elements(by=By.CLASS_NAME, value="source-and-time")
# date = trend_bot.find_elements(by=By.CLASS_NAME, value="source-and-time")

for t, s, src in zip(trends, search_count, source):
    print(f"TREND: {t.text}\nSEARCH COUNT:{s.text}\nSOURCE and DATE: {src.text}\n\n")

