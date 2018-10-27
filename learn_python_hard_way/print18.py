#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 命名,变量,代数和函数


# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))


# ok, that *argv is actually pointless, we just do this
def print_two_again(arg1,arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))


# this just takes one argument
def print_one(arg1):
    print("arg1: %r" % arg1)


# this one takes no arguments
def print_none():
    print("I got nothin")

print_two("aaa","bbb")
print_two_again("zend", "shaw")
print_one('Frist')
print_none()