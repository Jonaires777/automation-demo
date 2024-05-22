import os
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

CPF_INPUT_XPATH = '//*[@id="accountId"]'
CONTINUE_BUTTON_XPATH = '//*[@id="enter-account-id"]'
PASSWORD_INPUT_XPATH = '//*[@id="password"]'
ENTER_BUTTON_XPATH = '//*[@id="submit-button"]'

async def handle_page_login(tab):
    
    cpf_input = await tab.select('#accountId')
    await cpf_input.send_keys(os.getenv("CPF"))
    
    continue_button = await tab.select('#enter-account-id')
    await continue_button.click()
    
    password_input = await tab.select('#password')
    await password_input.send_keys(os.getenv("PASSWORD"))

    enter_button = await tab.select('#submit-button')
    await enter_button.click()
    
    print("Logged successfully")
    
    return tab
    