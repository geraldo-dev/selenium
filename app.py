from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

drive = webdriver.Edge()

drive.get('https://www.mercadolivre.com.br/')


search_name = drive.find_element(By.NAME, 'as_word')
search_name.send_keys('notebook')

search_btn = drive.find_element(By.CLASS_NAME, 'nav-search-btn').click()

sleep(2)
cards = drive.find_elements(By.CLASS_NAME, 'ui-search-result__wrapper')
price = 'price-tag-fraction'
freete = 'ui-search-item__shipping--free'
description = 'ui-search-item__title'

for card in cards:
    print('price: ', card.find_element(By.CLASS_NAME, price).text)
    print('freete: ', card.find_element(By.CLASS_NAME, freete).text)
    print('description: ', card.find_element(By.CLASS_NAME, description).text)

sleep(5)

drive.close()