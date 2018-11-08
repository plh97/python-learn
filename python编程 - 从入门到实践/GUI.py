#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 正则表达式；练习

from tkinter import *

def resize(ev=None):
    label.config(font='Helvetica -%d bold' % \
	scale.get())

top = Tk()
top.geometry('250x240')

label = Label(top, text="Hello", font="Helvetica -12 bold");
label.pack(fill=Y, expand=1)

scale = Scale(top, from_=10,to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)

quit = Button(top,text = 'hello world',command = top.quit,bg='red',fg='white')

label.pack()

mainloop()