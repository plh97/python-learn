#!/usr/bin/python
# -*- coding: UTF-8 -*-




def fib(n):
	if(n==1 or n==2):
		return 1
	else:
		return fib(n-1) + fib(n-2)


print(fib(42))