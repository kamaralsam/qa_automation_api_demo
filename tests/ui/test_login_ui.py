from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.saucedemo.com/"


def test_valid_login_navigates_to_inventory(browser):
    browser.get(BASE_URL)

    username = browser.find_element(By.ID, "user-name")
    password = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.ID, "login-button")

    username.clear()
    password.clear()

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    wait = WebDriverWait(browser, 10)
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    assert "/inventory.html" in browser.current_url
