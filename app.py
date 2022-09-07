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

datas = []

for card in cards:
    datas.append({
        'price' : card.find_element(By.CLASS_NAME, 'price-tag-fraction').text,
        'frete': card.find_element(By.TAG_NAME, 'p').text,
        'description': card.find_element(By.TAG_NAME, 'h2').text
    })

sleep(2)

print(datas)

drive.close()