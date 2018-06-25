#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 正则表达式；练习

import re
import os

str = '你们好  我的是啥  啥也不是'

f = re.findall('\w+', str,)

print(f)