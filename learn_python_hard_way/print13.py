#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 参数,解包和变量


from sys import argv


script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your first variable is: %r" % (
    input()
)
print "your second variable is:", second
print "your third variable is:", third



# argv 和 raw_input 区别, 一个在运行开始就要输入,另一个在运行过程中才要输入.