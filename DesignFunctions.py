#function file
import turtle
bob = turtle.Turtle()
bob.speed(0)

def polygon1(s,d):
    angle=360/s
    bob.color(c)
    for times in range(s):
        bob.forward(d)
        bob.right(angle)

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(distance):
    bob.color(c)
    for times in range(5):
        bob.forward(distance)
        bob.right(144)

def line(d,a,times):
    for times in range(times):
        bob.color("white")
        bob.forward(d)
        bob.right(a)
    
def line1(d,a,times):
    for times in range(times):
        bob.color("white")
        bob.forward(d)
        bob.left(a)


def circle(r):
    bob.begin_fill()
    bob.color("white")
    bob.circle(r)
    bob.fillcolor("white")
    bob.end_fill()
