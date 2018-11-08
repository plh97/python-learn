#!/usr/bin/python
# -*- coding: UTF-8 -*-

d = {}

d['a'] = '23423'
d['d'] = 'dirctionary'

for key,val in d.items():
	print "{"+key+": "+val.decode('utf-8')+"}"