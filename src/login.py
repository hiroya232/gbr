import os
from dotenv import load_dotenv


async def transition_to_login(pages):
    await pages.goto('http://game.granbluefantasy.jp/#authentication', waitUntill=['domcontentloaded'])
    await pages.waitForSelector('#mobage-login')
    await pages.click('#mobage-login')


async def login(pages):
    load_dotenv('.env')
    await pages.type('#subject-id', os.environ.get('MOBAGE_ID'))
    await pages.type('#subject-password', os.environ.get('MOBAGE_PASSWORD'))
    await pages.waitFor(1000)
    await pages.click('#login')


async def close_login_tab(pages):
    await pages.waitForSelector('#notify-response-button')
    await pages.click('#notify-response-button')
