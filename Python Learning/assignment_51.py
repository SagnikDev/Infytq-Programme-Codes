from turtle import *

wn = Screen()
wn.setup(500,500)
turtle = Turtle()
turtle.speed("fastest")

step = 100
def draw_square(length,angle):
    for i in range (0,step):
        for b in range (0,4):
            turtle.forward(length+i)
            turtle.right(angle+b)

draw_square(100,90)
