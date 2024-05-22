import math
import random
import nodriver
import undetected_chromedriver as undetected_driver
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait

TIMEOUT_IN_SECONDS = 30

def init_undetected_driver(arguments: list[str]):
    webdriver_options = undetected_driver.ChromeOptions()

    for argument in arguments:
        webdriver_options.add_argument(argument)

    browser = undetected_driver.Chrome(
        options=webdriver_options, enable_cdp_events=True, version_main=124
    )
    waiter = WebDriverWait(browser, TIMEOUT_IN_SECONDS)

    return browser, waiter

async def init_nodriver():
    browser = await nodriver.start(
        headless=False,
    )
    
    return browser

def init_standard_driver(arguments: list[str]):
    webdriver_options = webdriver.ChromeOptions()

    for argument in arguments:
        webdriver_options.add_argument(argument)

    browser = webdriver.Chrome(options=webdriver_options)
    waiter = WebDriverWait(browser, TIMEOUT_IN_SECONDS)

    return browser, waiter

async def init_web_driver(arguments: list[str], undetected=False, nodriver=False):
    if nodriver:
        return await init_nodriver()
    
    if undetected:
        return init_undetected_driver(arguments)

    return init_standard_driver(arguments)
