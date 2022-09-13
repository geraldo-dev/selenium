from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from time import sleep

opitons = Options()
opitons.add_argument('--headless')

drive = webdriver.Edge(options=opitons)

#primeiro entra no site
drive.get('https://www.mercadolivre.com.br/')

sleep(2)
#segundo procura um produto
#pega dados
#teceiro e par o proximo produto

datas = []

search_name = drive.find_element(By.NAME, 'as_word')
search_name.send_keys('notebook')

search_btn = drive.find_element(By.CLASS_NAME, 'nav-search-btn').click()

boxs = drive.find_elements(By.CLASS_NAME, 'ui-search-result__wrapper')


for box in boxs:
    datas.append({
        'price' : box.find_element(By.CLASS_NAME, 'price-tag-fraction').text,
        'frete': box.find_element(By.TAG_NAME, 'p').text,
        'description': box.find_element(By.TAG_NAME, 'h2').text
    })

print(datas)

drive.close()