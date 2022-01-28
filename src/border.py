import asyncio
from pyppeteer import connect


async def main():
    browser = await connect(browserWSEndpoint='ws://host.docker.internal:9222/devtools/browser/6dbbf347-a599-473c-a8cc-24fdd1aa3aad')

    pages = await browser.pages()
    await pages[-1].goto('http://game.granbluefantasy.jp/#authentication', waitUntill=['domcontentloaded'])

    await pages[-1].waitForSelector('#mobage-login')
    await pages[-1].click('#mobage-login')

asyncio.get_event_loop().run_until_complete(main())
