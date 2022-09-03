from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

brownser = webdriver.Edge()

brownser.get('https://www.youtube.com/')

search_query = brownser.find_element(By.NAME, 'search_query')
search_query.send_keys('metallica seek and destroy')
search_query.send_keys(Keys.RETURN)

sleep(1)
lnk = brownser.find_element(By.LINK_TEXT, 'Metallica - Seek And Destroy (HD)')
lnk.click()

#like
sleep(3)
brownser.close()