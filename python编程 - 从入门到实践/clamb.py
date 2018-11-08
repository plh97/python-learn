#!/usr/bin/python
# -*- coding: UTF-8 -*-

import asyncio
from pyppeteer import launch
import re
import time


async def main():
    browser = await launch({
        "executablePath": "C:/Users/33318/AppData/Local/Google/Chrome SxS/Application/chrome.exe",
        "timeout": 0,
        "headless": False,
        "slowMo": 1,
    })
    page = await browser.newPage()
    await page.setViewport({ "width": 1566, "height": 768 })

    # await page.goto('https://juejin.im/post/5b2fcdbbe51d4558817e0dd8')
    await page.goto('https://github.com/KevinHock?page=2&tab=following')
    button = await page.querySelector('.position-relative button')
    info = await page.evaluate('(button) => button.click()', button)

    print(info)
    time.sleep(1000)


    # for num in range(0,20000):  # 迭代 10 到 20 之间的数字
        # time.sleep(1)
        # await page.reload()
    # await browser.close()

asyncio.get_event_loop().run_until_complete(main())
