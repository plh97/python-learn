#!/usr/bin/python
# -*- coding: UTF-8 -*-

# branch of function or condition

from sys import exit

# 黄金屋
def gold_room():
    print("This room is full of gold. How much do you take?")

    next = raw_input("> ")


    
    if next.isdigit():
        how_much = int(next)
    else:
        print("Man, learn to type a number. give you last chance to type again!!")
        print "=============================="
        gold_room()
    
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

# 熊屋
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_move = False

    # 无限循环的一段话
    while True:
        print("1.take honey")
        print("2.taunt bear")
        print("3.open door")
        next = raw_input("> ")
        if next == "take honey" or next == '1':
            dead("The bear look at you then slaps your face off.")
        elif (next == "taunt bear" or next == '2') and not bear_move:
            print("The Bear has moved from the door. You can go through it now.")
            bear_move = True
        elif  (next == "taunt bear" or next == "2") & bear_move:
            dead("The bear gets pissed off and chews your leg off.")
        elif  (next == "open door" or next == "3") & bear_move:
            gold_room()
        else:
            print("I got no idea what that means.")




# 邪神屋
def cthulhu_room():
    print('Here you see the great evil Cthulhu.')
    print('He, it, whatever stares at you and you go insane.')
    print('Do you flee for your life or eat your head?')

    print('1.flee')
    print('2.head')
    next = raw_input('> ')

    if "flee" in next or next == '1':
        start()
    elif "head" in next or next == '2':
        dead("Well that was tasty!")
    else: 
        cthulhu_room()





# 死亡函数
def dead(why):
    print('%r Good job!' % why)
    exit(0)




# 初始化函数
def start():
    print('You are in a dark room.')
    print("There is a door to your right and left.")
    print('which one do you take?')
    print('1.left')
    print('2.right')

    next = raw_input('> ')

    if next == '1' or next == 'left':
        bear_room()
    elif next == '2' or next == 'right':
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

# 初始化
start()