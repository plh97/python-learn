#!/usr/bin/python
# -*- coding: UTF-8 -*-

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\nno a line"
backslash_cat = "I'am \\ a \\ cat."

fat_cat = """
I';; do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""


print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


print '''
转义字符          功能
    \\\         反斜杠(\)
    \\'         单引号(\')
    \\"         双引号(\")
    \\a         ASCII响铃符(BEL)
    \\b         ASCII退格符(BS)
    \\f         ASCII进纸符(FF)
    \\n         ASCII换行符(LF)
    \\N{name}   Unicode数据库中的字符名,其中name是它的名字,仅适用Unicode
    \\r         ASCII回车符(CR)
    \\t         ASCII水平制表符(TAB)
    \\uxxxx     值为16位进制xxxx的字符(仅适用Unicode)
    \\Uxxxxxxxx 值为32位进制xxxxxxxx的字符(仅适用Unicode)
    \\v         ASCII垂直制表符(VT)
    \\ooo       值为8进制值ooo的字符(VT)
    \\xhh       值为16进制值hh的hh的字符(VT)
'''

# 无限循环数字
# while True:
#     for i in ["/","-","|","\\","|"]:
#         print "%s\r" % i