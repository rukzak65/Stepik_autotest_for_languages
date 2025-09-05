import time

import pytest
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_cart_add(browser):
    browser.get(link)
    btn_found = False
    try:
        browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        btn_found = True
        time.sleep(5)

    except:
        pass

    assert btn_found == True, f"Кнопка добавления в корзину не найдена на странице"
