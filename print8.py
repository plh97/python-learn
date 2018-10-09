#!/usr/bin/python
# -*- coding: UTF-8 -*-

formatter = "%r %r %s %r"


print formatter % (1,2,3,4)
print formatter % ("1","2","3","4")
print formatter % ("one","two","three","four")
print formatter % (True, False ,True ,False)
print formatter % (formatter,formatter,formatter,formatter)



# 当你打印的是非 ASCII(American Standard Code for Information Interchange)字符 
# 使用%r会打印 ->  \xe4\xbd\xa0 
# 解决方案 用 %s
print formatter % (
    "i had an pen",
    "i ewf",
    "i 你",
    "i ewf",
)