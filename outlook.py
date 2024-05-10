import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException

user_agents = [
    # Firefox
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
    # Safari
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (iPad; CPU OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 Safari/604.1",
    # Edge
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
    # Opera
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.277",
    # Internet Explorer
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    # Android
    "Mozilla/5.0 (Linux; Android 11; Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    # iOS
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1"
]

topics = [
    "Inspiring Quotes",
    "Tech Tips",
    "Daily Wisdom",
    "Health & Wellness",
    "Productivity Hacks",
    "Travel Adventures",
    "Book Recommendations",
    "Recipe of the Day",
    "Financial Insights",
    "Motivational Stories",
    "Little reflexion"
]

messages = [
    "Hey there! Here's a quote to kickstart your day: 'The only way to do great work is to love what you do.' - Steve Jobs",
    "Hi! Did you know that you can use Ctrl + Shift + T to reopen the last closed tab in your browser? It's a lifesaver!",
    "Hello! Remember, 'The only limit to our realization of tomorrow will be our doubts of today.' - Franklin D. Roosevelt",
    "Good morning! Don't forget to take a few minutes for yourself today. Self-care is important!",
    "Hey! Want to boost your productivity? Try the Pomodoro Technique: work for 25 minutes, then take a 5-minute break.",
    "Hi there! Dreaming of your next getaway? Explore local hidden gems for a unique travel experience!",
    "Hello! Looking for a good read? Check out 'The Alchemist' by Paulo Coelho for some profound insights.",
    "Good morning! Craving something delicious? Try this easy recipe for avocado toast with a twist!",
    "Hey! Take control of your finances today. Small savings add up over time!",
    "Hello! Need a little pick-me-up? Read about how perseverance leads to success. You've got this!",
    "The capacity of the human mind and body to adapt to all situations is infinite..."
]

""" Choosing a random user agent """
random_user_agent = random.choice(user_agents)

random_topic = random.choice(topics)

random_message = random.choice(messages)

options = Options()

""" Picking the random user agent and using as a valid u.a """
options.add_argument(f"--user-agent={random_user_agent}")

""" Enabling execute the action without the parse certificate """
options.add_experimental_option('excludeSwitches', ['enable-logging'])

""" The browser will be kept open with this option """ 
options.add_experimental_option("detach", True)

""" Instantiating the driver """
driver = webdriver.Chrome(options=options)

""" Getting the url to enter outlook """
try:
    driver.get('https://outlook.live.com/mail/0/?cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&nlp=1&RpsCsrfState=6d00a139-cf1a-9956-1f9c-9fa5ef8c7cb9&url=%2fowa%2f0%2f%3fcobrandid%253dab0455a0-8d03-46b9-b18b-df2f57b9e44c%2526nlp%253d1%2526RpsCsrfState%253d6d00a139-cf1a-9956-1f9c-9fa5ef8c7cb9')

    """ Setting selenium to wait 10 seconds before raising and exception """
    driver.implicitly_wait(10)  

    """ Login in Outlook """
    login = driver.find_element(By.XPATH, "//input[@name='loginfmt']")
    login.send_keys("ex4mple123@outlook.com")
    next_button = driver.find_element(By.XPATH, "//button[@id='idSIButton9']")
    next_button.click()
    password = driver.find_element(By.XPATH, "//input[@name='passwd']")
    password.send_keys("example123")
    enter_button = driver.find_element(By.XPATH, "//button[@id='idSIButton9']")
    enter_button.click()
    accept_button = driver.find_element(By.XPATH, "//button[@id='acceptButton']")
    accept_button.click()

    """ Accessing the button to send a new email """
    try:
        new_email_button = driver.find_element(By.XPATH, "//button[@aria-label='Novo email']")
        new_email_button.click()
    except StaleElementReferenceException:
        new_email_button = driver.find_element(By.XPATH, "//button[@aria-label='Novo email']")
        new_email_button.click()

    """ Accessing the destinatary """
    new_destinatary = driver.find_element(By.XPATH, "//div[@aria-label='Para']")
    new_destinatary.send_keys("airesjonathan123@outlook.com")

    """ Creating a topic """
    new_topic = driver.find_element(By.XPATH, "//input[@aria-label='Adicionar um assunto']")
    new_topic.send_keys(f"{random_topic}")

    """ Creating the message """
    new_message = driver.find_element(By.XPATH, "//div[@aria-label='Corpo da mensagem, pressione Alt+F10 para sair']")
    new_message.send_keys(f"{random_message}")

    """ Sending the email """
    send_email_button = driver.find_element(By.XPATH, "//button[@aria-label='Enviar']")
    send_email_button.click()

finally:
    time.sleep(5)
    
    driver.quit()