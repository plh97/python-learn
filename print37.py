#!/usr/bin/python
# -*- coding: UTF-8 -*-

# type of data

class A():
    pass


class B(A):
    pass


# ('Strings', <type 'str'>)
print('Strings',type('str'))   

# ('Number', <type 'int'>)
print('Number',type(111))  

# ('Float', <type 'float'>)
print('Float',type(1.2))

# ('Boolean', <type 'bool'>)
print('Boolean',type(True))

# ('None', <type 'NoneType'>)
print('None',type(None))

# ('List', <type 'list'>)
print('List',type([1,2,34,5]))

# ('Class', <type 'classobj'>)
print('Class',type(A()) == A)

# ('Class', <type 'classobj'>)
print('Class',type(B()) == B)
# true
print('Class',isinstance(B(),A))



print("\\\'123")

print "---\a\a\a\a\a\a\a\a\a\a\a---"
print "---\b\b\b\b\b\b\b\b\b\b\b---"
print "---\f---"
print "---\n---"
