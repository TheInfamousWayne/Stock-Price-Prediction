import bs4 as bs
from selenium import webdriver
browser = webdriver.Chrome()
url = ("https://www.google.com/finance?q=tsla")
browser.get(url)
html_source = browser.page_source
browser.quit()
soup = bs.BeautifulSoup(html_source, "lxml")
for el in soup.find_all("div",{'class':'_xLw'}):
    print(el.get_text())



import time
from selenium import webdriver
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://www.google.com/finance?q=tsla');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()




# *********************************  GO TO GOOGLE FINANCE AND SCRAPE THE NEWS **************************

import sys
sys.path.append("D:/Python Codes/Stock Price Prediction") #location to senti.py
from senti import get_sentiment

import bs4 as bs
import time
from selenium import webdriver
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://www.google.com/finance?q=appl');
time.sleep(2) # Let the user actually see something!
news_tab = driver.find_element_by_xpath('//*[@id="sh_uid_0"]/g-tabs/div/div/div[2]/div/div')
news_tab.click()
# now the driver is linked to this new page we have got after clicking
html_source = driver.page_source
soup = bs.BeautifulSoup(html_source, "lxml")
for el in soup.find_all("div",{'class':'_xLw'}):
    print(el.get_text())
    get_sentiment(el.get_text())
    print('\n')
time.sleep(5) # Let the user actually see something!
driver.quit()