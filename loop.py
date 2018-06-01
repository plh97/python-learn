#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = [334,234,34]

total = 0
for b in a:
	print b
	total = total + b
print total

print '小于100 ，同时可以被3，5整除的数'.decode('utf-8')

a = list(range(1, 100))

b = []

tot1 = 0
for e in a:
    if e % 3 == 0 or e % 5 == 0:
		b.append(e)
		tot1+=e
print b
print tot1

print '--------------------------'

i = 0
toti = 0
while i<6:
	toti += i
	i += 1

print toti