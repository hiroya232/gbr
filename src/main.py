import asyncio
import threading
from time import sleep
from pyppeteer import connect
import os
from dotenv import load_dotenv
import schedule

from login import *
from border import *

HOLDING_PERIOD_DATE = 7
INTERVAL_MINUTES_OF_GET_BORDER = 20
NUM_OF_TIMES_GET_BORDER = int(1440 * HOLDING_PERIOD_DATE / INTERVAL_MINUTES_OF_GET_BORDER)

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

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

    for i in range(NUM_OF_TIMES_GET_BORDER):
        schedule.every(20).minutes.do(run_threaded, await get_ranking_border(pages[-1]))
        sleep(1200) # TODO:これがなくても機能するようにする

    while True:
        schedule.run_pending()
        sleep(1)

asyncio.get_event_loop().run_until_complete(main())
