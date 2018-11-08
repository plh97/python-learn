
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# type of data

# A Simple Python program to demonstrate working 
# of yield 
  
# A generator function that yields 1 for first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
  
# Driver code to check above generator function 
for value in simpleGeneratorFun():  
    print(value) 


for value in simpleGeneratorFun():  
    print(value) 
