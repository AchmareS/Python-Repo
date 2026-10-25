import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium import webdriverwait

@pytest.mark.skip(reason="Skipping this test case")
def test_module1():
    assert 1==1


@pytest.mark.sanity
def test_module2():
    assert 1==2 ,"Intentional failed test case"

@pytest.mark.skipif(1==2, reason="Skipping this test case")
def test_new1():
    assert 1==1 

@pytest.mark.xfail
def test_webappopen():
    print("test demo web app open  ")
    driver = webdriver.Chrome();
    driver.get("https://www.google.com")

@pytest.mark.sanity
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
    #driver.quit()'
  


@pytest.fixture
def test_demo_fixture():
    print("text demo fixture")
