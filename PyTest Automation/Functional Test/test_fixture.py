
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



# @pytest.fixture()
# def fixture_logic():
#     print("test demo fixture logic")


@pytest.fixture
def driver():
    print("initilizing chrome broswer")
    driver = webdriver.Chrome()
    driver.get("https://jqueryui.com/")
    driver.maximize_window()

    yield driver

    print("closing browser")
    driver.quit()
    driver.close()

# def test_01(fixture_logic):
#     print("first test case")




def test_1_Naviagte_to_webapp(driver):
   driver.maximize_window
   
#    driver.get("https://jqueryui.com/slider/")
   driver.implicitly_wait(10)

def test_02_click_demo_button(driver):
    print("calling test 01 via test 02")
    test_1_Naviagte_to_webapp(driver)
    print("Tets 01 call succesfully completed")
    driver.implicitly_wait(10)
    element =  driver.find_element(By.XPATH,"//a[normalize-space()='Demos']")
    element.click()
    print("test sucessfully pass")

def test_03_dropable(driver):
    #driver.implicitly_wait(10)
    elememt = driver.find_element(By.XPATH,"//a[text()='Droppable']")
    elememt.click()

    
    #wait.until(lambda driver: driver.find_element(By.ID,'draggable'))

    element1 = driver.find_element(By.ID,'draggable')

    #wait.until(lambda driver: driver.find_element(By.ID,'droppable'))
    elememt2 = driver.find_element(By.ID,'droppable')

    action = ActionChains(driver)
    action.drag_and_drop(element1,elememt2).perform()
    
    