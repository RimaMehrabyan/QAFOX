from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(scope='module')
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1018")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def login(driver):
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
    driver.find_element(By.NAME, 'email').send_keys("rimamehrabyan@gmail.com")  # Use a valid email
    driver.find_element(By.NAME, 'password').send_keys("RimaQA2024/")  # Use the corresponding password
    driver.find_element(By.XPATH, '//input[@value="Login"]').click()