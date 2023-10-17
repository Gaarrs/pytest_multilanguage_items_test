import pytest
import selenium
import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_quest_should_see_add_to_basket(browser):
    browser.get(link)

    add_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert add_button is not None, "Button not found"
