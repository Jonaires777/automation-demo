from dotenv import load_dotenv
from handle_page_access import handle_page_access
from handle_login import handle_page_login

from utils import init_web_driver


def main():
    load_dotenv()
    
    browser, waiter = init_web_driver([], undetected=True)
    
    print("Browser initiated sucessfully")

    handle_page_access(browser, waiter)

    handle_page_login(browser, waiter)    
    
main()