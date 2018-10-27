#!/usr/bin/python
# -*- coding: UTF-8 -*-

# list operation

numbers = []

numbers.append(123)

# 上面代码经历三个步骤
# 1.找到numbers变量
# 2.查看numbers内部的变量,找到append
# 3.当看到append后面跟着(),python立刻发现,这个是一个函数,需要执行.
# 4.append函数立即执行,并且携带参数, append(numbers,123),
# 默认第一个参数是他自己,只不过影藏了.因此就变成了append(123)



print numbers






ten_thing = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_thing.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", stuff)
    stuff.append(next_one)
    print("There's %d item now." % len(stuff))

print("There we go: " , stuff)

print("Let's do some things with stuff.")

print stuff[1]
print stuff[-1]

stuff.pop()

print(" ".join(stuff)) # what's cool!
print("#".join(stuff[3:5])) # what's cool!



print ' - '.join('aaaa')