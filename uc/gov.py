import nodriver
from dotenv import load_dotenv
from handle_page_access import handle_page_access
from handle_login import handle_page_login
from handle_task import handle_task
from handle_sign import handle_sign

from utils import init_web_driver


async def main():
    load_dotenv()
    
    browser = await init_web_driver([], nodriver=True)
    
    print("Browser initiated sucessfully")

    tab = await handle_page_access(browser)

    await handle_page_login(tab)    
    
    #handle_task(browser, waiter)
    
    await handle_sign(browser)
    
if __name__ == "__main__":
    # since asyncio.run never worked (for me)
    # i use
    nodriver.loop().run_until_complete(main())