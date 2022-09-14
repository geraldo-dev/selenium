from pydoc import classname
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from time import sleep
from bs4 import BeautifulSoup as bs

opitons = Options()
opitons.add_argument('--headless')

drive = webdriver.Edge(options=opitons)

name_product = ['notebook dell','notebook positivo','notebook ace']
#primeiro entra no site
drive.get('https://lista.mercadolivre.com.br/'+name_product[0])
sleep(2)
#teceiro e par o proximo produto
page = bs(drive.page_source, 'html.parser')

list_products = []


boxss = page.find_all('span', {'class':'price-tag-fraction'}) 
# print('-->', boxs)
print('-->', boxss)
# for produto in list_products_find:
#     print('-->', produto)
#     #segundo procura um produto
#     search_name = drive.find_element(By.NAME, 'as_word')
#     search_name.send_keys('notebook dell')
#     search_name.click()
    #li class ui-search-result__wrapper
    #span class price-tag-fraction
    #p class ui-search-item__shipping ui-search-item__shipping--free
    #h2 class ui-search-item__title ui-search-item__group__element shops-custom-secondary-font

    # search_btn = drive.find_element(By.CLASS_NAME, 'nav-search-btn').click()

    # boxs = page.find_all('div', class_="ui-search-result__content-wrapper shops-custom-secondary-font")
    # print('....',boxs)

    # sleep(1)
    # for box in boxs:
    #     #pega dados
    #     list_products.append({
    #         'price' : box.find_element(By.CLASS_NAME, 'price-tag-fraction').text,
    #         'frete': box.find_element(By.CLASS_NAME, 'ui-search-item__shipping ui-search-item__shipping--free').text,
    #         'description': box.find_element(By.CLASS_NAME, 'ui-search-item__title ui-search-item__group__element shops-custom-secondary-font').text
    #     })
    # search_name.clear()
    # sleep(1)

# print(list_products)

drive.close()