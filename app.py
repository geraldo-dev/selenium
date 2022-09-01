from selenium import webdriver
from time import sleep

brownser = webdriver.Edge()

brownser.get('https://www.instagram.com/geraldo_fnt/')

sleep(3)

brownser.quit()