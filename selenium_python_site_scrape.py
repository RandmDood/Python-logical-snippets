from selenium import webdriver
from selenium.webdriver.common.by import By

porg = webdriver.Chrome()

# wait command to give browser time to load webpage for all elements to be available for scraping
porg.implicitly_wait(13)
d = porg.get("https://python.org")

# narrowing down anchor element from unique class value "event-widget". higher sustainability
evet = porg.find_elements(by=By.CLASS_NAME, value="event-widget a")

# narrowing down using a somewhat absolute path. susceptible to damage due to the slightest change in html code
dayt = porg.find_elements(by=By.CLASS_NAME, value="event-widget > div > ul > li > time")


event_links = []
dates = []
# creating liat of events and dates with data scraped from the python.org website
for e,d in zip(evet, dayt):
    event_url = (e.get_attribute("href"))
    event_links.append(event_url)
    date_time = (d.get_attribute("datetime"))[:10]
    dates.append(date_time)


n = 0
events = []
# to create a dictionary using data from event list and date list
for e, d in zip(event_links, dates):
    event_dict = {n: {f"event-URL: {e}, date: {d}"}}
    n += 1
    events.append(event_dict)

print(events)

porg.quit()
