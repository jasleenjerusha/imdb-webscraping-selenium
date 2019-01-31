from selenium import webdriver #importing webdriver 
from selenium.webdriver.common.keys import Keys

import os #importing the os module
fd=open("MovieInfo.txt","w+") #opening text file for writing

#driver = webdriver.Chrome('/home/jerusha/chromedriver_linux64(1)/chromedriver')#opening browser
driver = webdriver.Chrome('./chromedriver')#opening browser
driver.get("http://www.imdb.com") #opening the website

elem = driver.find_element_by_name("q") #finding the search box in the website by inspecting
elem.clear() #clearing the search box
elem.send_keys("Forrest Gump") 
elem.send_keys(Keys.RETURN)#to click enter button i.e., to search the movie name
assert " No Results Found" not in driver.page_source

title = driver.find_element_by_link_text("Forrest Gump").click()
info = driver.find_elements_by_xpath('//*[@id="title-overview-widget"]/div[1]/div[2]')
for information in info:
    print(information.text) #printing in terminal
    fd.write(information.text) # writing to a text file
#driver.close()
