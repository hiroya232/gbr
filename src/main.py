import asyncio
from pyppeteer import connect
import os
from dotenv import load_dotenv

from login import *
from border import *


async def main():
    load_dotenv('.env')
    browser = await connect(browserWSEndpoint=os.environ.get('BROWSER_WS_ENDPOINT'))

    pages = await browser.pages()
    await transition_to_login(pages[-1])

    await pages[-1].waitFor(1000)

    pages = await browser.pages()
    await login(pages[-1])

    await close_login_tab(pages[-1])

    await pages[-1].waitFor(1000)

    pages = await browser.pages()
    await get_ranking_border(pages[-1])

asyncio.get_event_loop().run_until_complete(main())
