from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from time import sleep

opitons = Options()
# opitons.add_argument('--headless')

drive = webdriver.Edge(options=opitons)

name_product = ['notebook','mouse','headphone']

#primeiro entra no site
drive.get('https://www.mercadolivre.com.br/')
sleep(2)

#busca produto
search_name = drive.find_element(By.NAME, 'as_word')
search_name.send_keys(name_product[0])

search_btn = drive.find_element(By.XPATH, '/html/body/header/div/form/button').click()
sleep(0.5)
#price-tag-fraction span price
ol = drive.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/ol[1]')

li = ol.find_elements(By.TAG_NAME, 'li')[0]
print('>>>', li.text)

sleep(3)
drive.close()