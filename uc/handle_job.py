import os
import time
import math
import undetected_chromedriver as undetected_driver
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from utils import save_page

def handle_job(browser: Chrome, waiter: WebDriverWait):

    jobs = []
    
    waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/header/div/div[2]/a/div/div/div[1]')
        )
    )
    
    search_job_button = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/div/div[1]/div[4]/a')
        )
    )
    search_job_button.click()
    
    job_table = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/div[2]/div[2]/div[2]/div/table/tbody')
        )
    )
        
    total_jobs = waiter.until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div/nav/div[2]/span[3]')
        )
    )
    
    number_of_clicks = math.ceil(int(total_jobs.text)/5)
    
    for i in range(number_of_clicks):
        time.sleep(2)
        
        rows = job_table.find_elements(By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/div[2]/div[2]/div[2]/div/table/tbody/tr')
        
        for row in rows:
            data = {}
            
            data["role"] = row.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[1]').text
            data["salary"] = row.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[2]').text
            data["locality"] = row.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[3]').text
            data["neighborhood"] = row.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[4]').text
            data["quantity"] = row.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]').text
            data["contract"] = row.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[6]').text
            data["date"] = row.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[7]').text
            
            jobs.append(data)
            
        pagination_button = waiter.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div/nav/div[4]/button[2]')
            )
        )
        pagination_button.click()
    
    print('Aqui está a sua lista de empregos!')
    print('')  
    
    for job in jobs:
        print('')
        print('*=======================*')
        print('       Informações       ')
        for key, value in job.items():
            print(f'{key}: {value}')
        print('*=======================*')
        print('')      
    print('Task finished!')
    
    
    