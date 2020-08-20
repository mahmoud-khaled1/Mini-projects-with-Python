import turtle

#make object name bob !
bob=turtle.Turtle()
#animation of object                               -
#bob.forward(100) # go 100 pixels                  -
#bob.left(45) # then turn left 45 angle           -
#bob.forward(200) # then go 100 pixel     ---------
#bob.right(100)
#bob.forward(100)

#bob.penup()# to remove lines that Draw behind the shape

#Draw  red Triangle
#bob.begin_fill() # to color inside triangle
#bob.color("blue","red") #color of triangle
#bob.forward(200)
#bob.left(120)
#bob.forward(200)
#bob.left(120)
#bob.forward(200)
#bob.end_fill()#to color inside triangle

#Draw star
#bob.color("red")
#bob.begin_fill()
#for i in range(10):

#    bob.forward(200)
#   bob.left(135)
#    bob.forward(200)

#bob.end_fill()

#Draw Sun
"""
bob.color("red")
bob.speed(10)

bob.begin_fill()

for i in range(200):
    bob.forward(200)
    bob.left(168.5)
bob.end_fill()
"""
#Draw Star with root star !

import turtle
scr=turtle.Screen()
scr.bgcolor("red")

sta=turtle.Turtle()

def star(st ,size):
    if size<=10:
        return
    else:
        for i in range(5):
            sta.forward(size)
            star(sta,size//2)
            sta.left(216)

star(sta,100)



#to told compiler that turtle finish here !
turtle.done()