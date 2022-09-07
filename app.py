from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

drive = webdriver.Edge()

drive.get('https://www.mercadolivre.com.br/')

sleep(3)

drive.close()