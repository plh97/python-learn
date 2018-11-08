#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 5
b = 23

if a <b:
	print 'a is smaller'
	print 'say something'
else:
	print 'a is bigger'


e = 6
f = 6

if e < f:
	pass
else:
	if e == f:
		print('they are equal')


name = 'peng'
height_m = 2
weight_kg = 60

bmi = weight_kg / (height_m ** 2)
print('bmi:')
print(bmi)

if bmi < 25:
	print(name,bmi)
	print('you are not overweigh')
else:
	print(name,bmi)
	print('you are overweigh')