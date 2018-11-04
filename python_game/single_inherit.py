#!/usr/bin/python
# -*- coding: UTF-8 -*-

### 单继承
class Point():
    x=0.0
    y=0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print('Point constructor')
    
    def ToString(self):
        return "{X: %d,Y: %d}" % (self.x, self.y)




class Circle(Point):
    radius = 0.0

    def __init__(self, x,y,radius):
        super(self).__init__(x,y)
        self.radius = radius
        print("Circle constructor")

    def ToString(self):
        return super(self).ToString() + \
            ", {RADIUS: %d}" % (self.radius)



class Geometry(Point):

    def __init__(self, x,y,radiuX, radiuY):
        super(self).__init__(x,y)
        self.radiusX = radiuX
        self.radiusY = radiuY
        print("Circle constructor")



p = Point(10,20)
print(p.ToString())
# {X: 10,Y: 20}

c = Circle(100,100,50)
print(c.ToString())
# {X: 100,Y: 100}, {RADIUS: 50}