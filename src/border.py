import asyncio
from pyppeteer import connect
import os
from dotenv import load_dotenv


async def login(pages):
    load_dotenv('.env')
    await pages.type('#subject-id', os.environ.get('MOBAGE_ID'))
    await pages.type('#subject-password', os.environ.get('MOBAGE_PASSWORD'))
    await pages.waitFor(1000)
    await pages.click('#login')


async def main():
    browser = await connect(browserWSEndpoint='ws://host.docker.internal:9222/devtools/browser/6dbbf347-a599-473c-a8cc-24fdd1aa3aad')

    pages = await browser.pages()
    await pages[-1].goto('http://game.granbluefantasy.jp/#authentication', waitUntill=['domcontentloaded'])

    await pages[-1].waitForSelector('#mobage-login')
    await pages[-1].click('#mobage-login')

    await pages[-1].waitFor(1000)

    pages = await browser.pages()
    await login(pages[-1])

asyncio.get_event_loop().run_until_complete(main())
