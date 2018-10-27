#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 把提示框当做变量

age = raw_input("how old are you? ")

height = raw_input("How tall are u")

weight = input("How mutch do u weight?")



print "so, u're %r old, %r tall and %r heavy." % (
    age, height, weight
)

# 当我打印 python -m pydoc raw_input

#           结果如下

# Help on built-in function raw_input in module __builtin__:

# raw_input(...)
#     raw_input([prompt]) -> string

#     Read a string from standard input.  The trailing newlineis stripped.
#     If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
#     On Unix, GNU readline is used if enabled.  The prompt string, if given,
#     is printed without a trailing newline before reading.




# pydoc 模块能从python中提取获得docstring信息

# at the same time  pydoc can run html
