#!/usr/bin/python
# -*- coding: UTF-8 -*-

import asyncio
from pyppeteer import launch
import re

async def main():
    browser = await launch({
        "executablePath": "C:/Users/33318/AppData/Local/Google/Chrome SxS/Application/chrome.exe",
        "timeout": 0,
        "headless": False,
        "slowMo": 1,
    })
    page = await browser.newPage()
    await page.goto('https://pipk.top')
    await page.screenshot({'path': 'pipk.png'})
    html = await page.evaluate('''() => {
        return document.body.outerHTML
    }''')
    result = re.match("http.*?comment/(.*?)", html)
    print(result, html)
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())
