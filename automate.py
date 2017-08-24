import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def init_driver():
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def lookup(driver, query1, query2):
    driver.get("https://gmail.com")
    try:
        username = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "identifier")))

        button_next = driver.wait.until(EC.element_to_be_clickable(
            (By.ID, "identifierNext")))
        username.send_keys(query1)
        button_next.click()

        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
            )

        pwd_next = driver.wait.until(EC.element_to_be_clickable(
        (By.ID, "passwordNext")))


        password.send_keys(query2)
        pwd_next.click()
    except TimeoutException:
        print("Box or Button not found in google.com")


if __name__ == "__main__":
    username=input('Enter your gmail username')
    password=input('Enter your password')
    driver = init_driver()
    lookup(driver,username,password)
    time.sleep(5)
    driver.quit()