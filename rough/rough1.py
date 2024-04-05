import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
import time
# Project library imports
from page_elements.GASB.page_pobjects import header, footer
from automated_actions import testactions, basicuseraction, techactions
from page_elements.GASB.gasb_url_txt import basic_url, contructed_url
from selenium.webdriver.common.action_chains import ActionChains

path = Service("C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe")
driver = webdriver.Chrome(service=path)
driver.maximize_window()
driver.implicitly_wait(20)
driver.get(basic_url.home)
time.sleep(3)

