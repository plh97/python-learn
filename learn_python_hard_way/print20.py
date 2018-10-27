#!/usr/bin/python
# -*- coding: UTF-8 -*-

# function and file


from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print str(("第%s行" % line_count))
    print(f.readline(),)



current_file = open(input_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print lines:")


current_line=1
while current_line<4:
    print_a_line(current_line, current_file)
    current_line += 1
    