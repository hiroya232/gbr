import asyncio
from pyppeteer import connect

from login import *
from border import *


async def main():
    browser = await connect(browserWSEndpoint='ws://host.docker.internal:9222/devtools/browser/6dbbf347-a599-473c-a8cc-24fdd1aa3aad')

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
