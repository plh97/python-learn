#!/usr/bin/python
# -*- coding: UTF-8 -*-

# python多进程编程；练习


from time import sleep, ctime

def loop1():
	print('我是进程1.1',ctime())
	sleep(4)
	print('我是进程1.2',ctime())

def loop2():
	print('我是进程2.1',ctime())
	sleep(2)
	print('我是进程2.2',ctime())

def main():
	print('我是主进程1.1',ctime())
	loop1()
	loop2()
	print('我是主进程1.2',ctime())



if __name__ == '__main__':
	main()
		