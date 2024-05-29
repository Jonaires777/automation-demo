from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

LOGIN_PAGE_TITLE_XPATH = "//*[@id='root']/div/main/div/div/div[1]/div/div/div/div[1]/div/div[1]/span"
LOGIN_ULR = "https://servicos.mte.gov.br/spme-v2/#/login"

def handle_page_access(browser: Chrome, waiter: WebDriverWait):
    browser.get(LOGIN_ULR)
    
    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, LOGIN_PAGE_TITLE_XPATH)
        )
    )
    
    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/div/div/div[1]/div/div[3]/button')
        )
    ).click()