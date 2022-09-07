from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

drive = webdriver.Edge()

drive.get('https://www.mercadolivre.com.br/')

search_name = drive.find_element(By.NAME, 'as_word')
search_name.send_keys('notebook')

search_btn = drive.find_element(By.CLASS_NAME, 'nav-search-btn').click()

sleep(5)

drive.close()