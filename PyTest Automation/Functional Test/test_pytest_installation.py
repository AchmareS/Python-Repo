import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium import webdriverwait

def test_module1():
    assert 1==1

def test_module2():
    assert 1==2 ,"Intentional failed test case"

def test_new1():
    assert 1==1 

def test_webappopen():
    print("test demo web app open  ")
    driver = webdriver.Chrome();
    driver.get("https://www.google.com")

def test_demo_web_app_open():
    print("test demo web app open")
    driver = webdriver.Chrome()
    driver.get("https://jqueryui.com")

    driver.maximize_window()
    #driver.find_element_by_xpath("//a[normalize-space()='Demos'])]").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"//a[normalize-space()='Demos']").click()
    driver.implicitly_wait(10)
    # wait = webdriverwait.WebDriverWait(driver, 10)
    #driver.quit()