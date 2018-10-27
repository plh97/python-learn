# #!/usr/bin/python
# # -*- coding: UTF-8 -*-

# # module class object

# # python is an OOP language

# # 类和模块是一回事,

# class MyStuff(object):
#     def __init__(self):
#         self.tangerine = "And now a thousnd years between"
    
#     def apple(self):
#         print "I AM CLASSY APPLES!"


# myStuff = {
#     'apple': 111,
#     'banana': 222,
#     'clity': 333
# }



# # 三种方法从某个东西里面获取内容
# # 字典
# myStuff['apple']

# # module 
# mystuff.apple()

# # class style
# myStuff = MyStuff()
# myStuff.apple()
# print myStuff.tangerine

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


happy_baby = Song([
    "Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there",
])


bulls_on_parade = Song([
    "They relly around the family",
    "With pockets full of shells",
])


happy_baby.sing_me_a_song()

bulls_on_parade.sing_me_a_song()