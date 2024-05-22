import os
import time
import nodriver as uc
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

SIGN_DOCUMENT_PAGE_URL = "https://assinador.iti.br/assinatura/index.xhtml"
PAGE_TITLE_XPATH = "//h1[contains(text(), 'Assinatura de documento')]"
FILE_INPUT_XPATH = "//*[@id='resultForm:uploadArquivo_input']"
SEND_FILE_BUTTON_XPATH = "//button[@type='submit']/span[contains(text(), 'Avançar')]"
SIGN_FILE_BUTTON_XPATH = "//button[@type='button']/span[contains(text(), 'Assinar')]"
CONFIRM_SIGN_BUTTON_XPATH = (
    '//*[@id="dlgAdicionarOutroDocumentoForm"]//span[contains(text(), "Assinar")]'
)

async def handle_sign(browser, file_path: str = "C:\\Users\\User\\automation-demo\\uc\\7 - metodologia agil.pdf"):
    tab = await browser.get(SIGN_DOCUMENT_PAGE_URL)
    
    await tab.select('h1')
    
    print("Sign page accessed successfully")

    file_input = await tab.select('.uploadArquivoClick input[type=file]')
    await file_input.send_keys(file_path)

    send_file_button = await tab.select('#resultForm\:j_idt256')
    await send_file_button.click()

    print("File uploaded successfully")

    sign_file_button = await tab.select('#dlgAdicionarOutroDocumentoForm\:j_idt336')
    await sign_file_button.click()

    """ confirm_sign_button = browser.find_element(By.XPATH, CONFIRM_SIGN_BUTTON_XPATH)
    confirm_sign_button.click()"""

    print("File entered the sign process successfully")