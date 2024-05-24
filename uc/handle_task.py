import os
import time
import undetected_chromedriver as undetected_driver
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

MAIN_PAGE_TITLE = '//*[@id="a4c5cb90-2f53-400c-82c0-7a6e2ffbedab"]/div/h2'
AUTH_INTERACTION = '//*[@id="barra-sso"]'
GET_CPF = '//*[@id="d8878bf7-f068-4bd0-aa20-283e0508ccad"]/div/div[2]/a[3]'
CPF_PAGE_TITLE = '//*[@id="content-core"]/div[2]/div[1]/div'
START_BUTTON = '//*[@id="content-core"]/div[2]/div[1]/a'
GET_INFORMATION_PAGE_TITLE = '//*[@id="rfb-main-container"]/h2'
CPF_INPUT = '//*[@id="txtCPF"]'
BIRTHDATE_INPUT = '//*[@id="txtDataNascimento"]'
HCAPTCHA = '//*[@id="hcaptcha"]/iframe'
SUBMIT_INFORMATION = '//*[@id="id_submit"]'

def handle_task(browser: Chrome, waiter: WebDriverWait):    

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
    
    get_cpf = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, GET_CPF)
        )
    )
    get_cpf.click()
        
    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, CPF_PAGE_TITLE)
        )
    )
    
    start_button = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, START_BUTTON)
        )
    )
    start_button.click()
        
    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, GET_INFORMATION_PAGE_TITLE)
        )
    )
    
    cpf_input = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, CPF_INPUT)
        )
    )
    cpf_input.send_keys(os.getenv('CPF'))
    
    time.sleep(2)
    
    birthdate_input = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, BIRTHDATE_INPUT)
        )
    )
    birthdate_input.send_keys(os.getenv('BIRTHDATE'))
    
    time.sleep(3)
        
    hcaptcha = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, HCAPTCHA)
        )
    )
    hcaptcha.click()
    
    time.sleep(5)
    
    submit_information = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, SUBMIT_INFORMATION)
        )
    )
    submit_information.click()

    print('Task finished successfully')
