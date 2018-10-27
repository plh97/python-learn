#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 展示 %d 可以用于展示后面的变量; 
x = "There are %d types of people." % 10
print x


# 用于展示两个变量
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
print y


# 你也可以直接打印变量 %r  -> r 会保留两边双引号
print "I said: %d." % x
print "I also said: %r" % y



# 你也可以直接打印布尔值
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"


print joke_evaluation % hilarious


# 可以直接打印两个变量相加
w = "This is the left side of..."
e = "a string with a right side"
print w+e





# %r -> 主要用于debug,因为它会显示原始数据
# %d -> 用于展示数字
# %s -> 用于展示字符串


