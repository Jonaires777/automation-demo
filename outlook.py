from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
""" Enabling execute the action without the parse certificate """
options.add_experimental_option('excludeSwitches', ['enable-logging'])

""" The browser will be kept open with this option """ 
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

""" Getting the url to enter outlook """
driver.get('https://outlook.live.com/mail/0/?cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&nlp=1&RpsCsrfState=6d00a139-cf1a-9956-1f9c-9fa5ef8c7cb9&url=%2fowa%2f0%2f%3fcobrandid%253dab0455a0-8d03-46b9-b18b-df2f57b9e44c%2526nlp%253d1%2526RpsCsrfState%253d6d00a139-cf1a-9956-1f9c-9fa5ef8c7cb9')

""" Login in Outlook """
login = driver.find_element(By.XPATH, "//input[@name='loginfmt']")
login.send_keys("ex4mple123@outlook.com")
next_button = driver.find_element(By.XPATH, "//button[@id='idSIButton9']")
next_button.click()
password = driver.find_element(By.XPATH, "//input[@name='passwd']")
password.send_keys("example123")
enter_button = driver.find_element(By.XPATH, "//button[@id='idSIButton9']")
enter_button.click()

""" Accessing the button to send a new email """
new_email_button = driver.find_element(By.XPATH, "//button[@aria-label='Novo Email']")
new_email_button.click()

""" Accessing the destinatary """
new_destinatary = driver.find_element(By.XPATH, "//div[@aria-label='Para']")
new_destinatary.send_keys("airesjonathan123@outlook.com")

""" Creating a topic """
new_topic = driver.find_element(By.XPATH, "//input[@aria-label='Adicionar um assunto']")
new_topic.send_keys("This is a test for automation")

""" Creating the message """
new_message = driver.find_element(By.XPATH, "//div[@aria-label='Corpo da mensagem, pressione Alt+F10 para sair']")
new_message.send_keys("Hi, this is an automated message")

""" Sending the email """
send_email_button = driver.find_element(By.XPATH, "//button[@aria-label='Enviar']")
send_email_button.click()

driver.quit()