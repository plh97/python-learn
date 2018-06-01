#!/usr/bin/python
# -*- coding: UTF-8 -*-

import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://pipk.top/article')
    await page.screenshot({'path': 'pipk.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
