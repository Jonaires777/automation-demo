from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

LOGIN_PAGE_TITLE_XPATH = "//*[@id='login-cpf']/h3"
LOGIN_ULR = "https://sso.acesso.gov.br/login?client_id=www.gov.br&authorization_id=18f82acb672"

def handle_page_access(browser: Chrome, waiter: WebDriverWait):
    browser.get(LOGIN_ULR)
    
    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, LOGIN_PAGE_TITLE_XPATH)
        )
    )