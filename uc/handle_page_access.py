from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

LOGIN_PAGE_TITLE_XPATH = "//*[@id='login-cpf']/h3"
LOGIN_ULR = "https://sso.acesso.gov.br/login"

async def handle_page_access(browser):
    tab = await browser.get(LOGIN_ULR)
    
    """ select = await tab.select('#barra-sso')
    await select.click() """
    
    await tab.select('#login-cpf h3')
    
    return tab