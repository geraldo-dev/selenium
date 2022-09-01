from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

brownser = webdriver.Edge()

brownser.get('https://www.youtube.com/')

tag = 'search_query'
elem = brownser.find_element(By.NAME, tag)

elem.send_keys('geraldo testando algo kkk')
sleep(2)
elem.send_keys(Keys.RETURN)


sleep(3)

brownser.quit()