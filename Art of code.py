import turtle
from DesignFunctions import *
turtle.colormode(255)
turtle.bgcolor(0,0,0)
bob.speed(0)

bob.width(10)
bob.speed(0)


jump(-500,500)
for times in range(255):
    c = (20,0,times+1)
    bob.color(c)
    bob.forward(1000)
    jump(-500,500-times*3)
jump(0,0)   


bob.width(1)


jump(-500,-150)
bob.begin_fill()
bob.color("white")
line1(5,3,20)
line(2,2,20)
line(5,4,20)
line1(4,3,25)
line1(7,2,25)
line(7,6,25)
line1(6,2,30)
line1(8,3,35)
line(7,6,25)


bob.right(20)
bob.forward(200)
bob.right(90)
bob.forward(982)
bob.right(95)
bob.forward(130)
bob.fillcolor("lightblue")
bob.end_fill()

jump(-500,-200)
bob.right(84)
bob.begin_fill()
bob.color("grey")
line(5,3,20)
line1(2,6,10)
line1(3,4,20)
line(8,4,20)
line(5,4,20)
line1(4,3,20)
line1(5,4,20)
line(4,4,15)
line(3,6,15)
line1(3,6,10)
line1(6,4,26)
line(8,4,30)
line1(2,3,15)
line1(2,3,20)
line(5,3,20)


bob.right(90)
bob.forward(210)
bob.right(90)
bob.forward(1010)
bob.right(93)
bob.forward(60)
bob.fillcolor("teal")
bob.end_fill()



jump(-350,100)
for times in range(1):      
    for planet in range(327):
        bob.color("lightcyan")
        bob.forward(planet-140)
        bob.left(planet-140)

jump(-320,40)
bob.width(2)
bob.color("white")
bob.goto(30,255)
bob.width(1)
jump(125,310)
for times in range(1):      
    for planet in range(327):
        bob.color("azure")
        bob.forward(planet-140)
        bob.left(planet-140)

jump(115,230)
bob.width(2)
bob.color("white")
bob.goto(230,123)
bob.width(1)
jump(320,130)
for times in range(1):      
    for planet in range(327):
        bob.color("snow")
        bob.forward(planet-140)
        bob.left(planet-140)

jump(70,80)
circle(2)
bob.goto(85,90)
circle(2)

jump(-220,300)
circle(2)
bob.goto(-235,275)
circle(2)

jump(280,450)
circle(2)
bob.goto(320,420)
circle(2)

jump(-50,100)
circle(2)
bob.goto(-90,130)
circle(2)

jump(-50,400)
circle(2)
bob.goto(-20,460)
circle(2)

jump(-420,180)
circle(2)
bob.goto(-450,210)
circle(2)

jump(-380,260)
circle(2)
bob.goto(-350,280)
circle(2)

jump(-250,240)
circle(2)
bob.goto(-280,269)
circle(2)

jump(200,300)
circle(2)
bob.goto(225,335)
circle(2)

jump(235,400)
circle(2)
bob.goto(195,435)
circle(2)

jump(50,40)
circle(2)
bob.goto(65,10)
circle(2)

jump(400,100)
circle(2)
bob.goto(410,120)
circle(2)

jump(430,180)
circle(2)
bob.goto(445,145)
circle(2)

jump(-200,-20)
circle(2)
bob.goto(-170,10)
circle(2)

jump(-250,25)
circle(2)
bob.goto(-225,45)
circle(2)

jump(370,120)
circle(2)
bob.goto(360,136)
circle(2)

jump(-135,180)
circle(2)
bob.goto(-170,160)
circle(2)

jump(200,-80)
circle(2)
bob.goto(165,-100)
circle(2)

jump(420,350)
circle(2)
bob.goto(360,335)
circle(2)

jump(320,30)
circle(2)

jump(320,32)
circle(3)

jump(-330,80)
circle(1.5)

jump(-270,33)
circle(1.5)

jump(293,40)
circle(1.5)

jump(-185,200)
circle(1.5)

jump(210,50)
circle(1.5)

jump(120,450)
circle(1.5)

jump(-190,420)
circle(1.5)

jump(-150,380)
circle(1.5)

jump(1000,1000)
