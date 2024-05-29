import os
import time
import undetected_chromedriver as undetected_driver
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from utils import save_page


MAIN_PAGE_TITLE = '//*[@id="a4c5cb90-2f53-400c-82c0-7a6e2ffbedab"]/div/h2'
AUTH_INTERACTION = '//*[@id="barra-sso"]'
SIGN_DOCUMENT = '//*[@id="barra-sso"]/sso-status-bar-section[2]/sso-status-bar-item[3]'
CPF_INPUT_XPATH = '//*[@id="accountId"]'
CONTINUE_BUTTON_XPATH = '//*[@id="enter-account-id"]'
PASSWORD_INPUT_XPATH = '//*[@id="password"]'
ENTER_BUTTON_XPATH = '//*[@id="submit-button"]'

def handle_sign(browser: Chrome, waiter: WebDriverWait):

    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, MAIN_PAGE_TITLE)
        )
    )
    
    get_auth = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, AUTH_INTERACTION)
        )
    )
    get_auth.click()
    
    sign_document = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, SIGN_DOCUMENT)
        )
    )
    sign_document.click()
    
    time.sleep(5)
    
    save_page(browser, open_screenshot=True)
    
    """ cpf_input = browser.find_element(By.XPATH, CPF_INPUT_XPATH)
    cpf_input.send_keys(os.getenv("CPF"))
    
    continue_button = browser.find_element(By.XPATH, CONTINUE_BUTTON_XPATH)
    continue_button.click()

    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, PASSWORD_INPUT_XPATH)
        )
    )
    
    password_input = browser.find_element(By.XPATH, PASSWORD_INPUT_XPATH)
    password_input.send_keys(os.getenv("PASSWORD"))

    enter_button = browser.find_element(By.XPATH, ENTER_BUTTON_XPATH)
    enter_button.click() """
    
    container = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/section[2]')
        )
    )
    
    global_content = container.find_element(By.XPATH, '//*[@id="resultForm"]/div[1]')
    
    result_panel = global_content.find_element(By.XPATH, '//*[@id="resultForm:resultPanel"]')
    
    result_doc_viewer = result_panel.find_element(By.XPATH, '//*[@id="resultForm:docViewer"]')
    
    upload_archive = result_doc_viewer.find_element(By.XPATH, '//*[@id="resultForm:uploadArquivo"]')
    
    """ choose_archive_button = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="resultForm:pn_opcoes"]/button')
        )
    )
    choose_archive_button.click() """
    
    input('Please, select the archive. If you already did it, press Enter')
    
    next_button = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="resultForm:j_idt256"]')
        )
    )
    next_button.click()
    
    sign_button = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="resultForm:j_idt257"]')
        )
    )
    sign_button.click()
    
    sign_button_popup = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="dlgAdicionarOutroDocumentoForm:j_idt336"]')
        )
    )
    sign_button_popup.click()
    
    input('Please, put the code you received on your govbr app. Then sign your document. If you did it press Enter')
    
    download_button = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="resultForm:downloadList:0:itemDownload"]')
        )
    )
    download_button.click()
    
    download_button_popup = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="j_idt301"]')
        )
    )
    download_button_popup.click()
    
    time.sleep(3)
    
    return_button = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="resultForm:btnVoltarPasso3"]')
        )
    )
    return_button.click()
    
    confirm_button = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="j_idt414"]')
        )
    )
    confirm_button.click()
    
    print('Task finished!')
    
    
    