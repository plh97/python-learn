# #!/usr/bin/python
# # -*- coding: UTF-8 -*-


# 隐式继承
# class Parent(object):
#     def implicit(self):
#         print("PARENT implict()")

# class Child(Parent):
#     pass

# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()


# 显示覆盖
# class Parent(object):

#     def override(self):
#         print("PARENT override()1")
    

# class Child(Parent):

#     def override(self):
#         print("CHILD override()2")
#         super(Child, self).override()
#         print("CHILD, AFTER PARENT altered()3")

        

# dad = Parent()
# son = Child()

# dad.override()
# son.override()


# 三种方式一起使用
# class Parent(object):
#     def override(self):
#         print("PARENT override()1")
#     def implicit(self):
#         print("PARENT implicit()1")
#     def altered(self):
#         print("PARENT altered()1")
    

# class Child(Parent):

#     def override(self):
#         print("CHILD override()2")
#         super(Child, self).override()
#         print("CHILD, AFTER PARENT altered()2")

#     def altered(self):
#         print("CHILD altered()2")
#         super(Child, self).altered()
#         print("CHILD, AFTER PARENT altered()2")

        

# dad = Parent()
# son = Child()

# print("="*20)

# dad.implicit()
# son.implicit()

# print("="*20)

# dad.override()
# son.override()

# print("="*20)

# dad.altered()
# son.altered()

# print("="*20)



# super & __init__ use together
# class Child(Parent):
#     def __init__(self, stuff):
#         self.stuff = stuff
#         super(Child, self).__init__()


# 合成
class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")
    

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()
    
    def overrider(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")


son = Child()
son.implicit()
son.overrider()
son.altered()

