#!/usr/bin/python
# -*- coding: UTF-8 -*-

import asyncio
from pyppeteer import launch

url = 'pipk.top/article'

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://'+url)
    await page.screenshot({'path': url+'.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
