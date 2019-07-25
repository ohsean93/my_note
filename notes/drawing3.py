import turtle
import random

turtle.colormode(255)

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.setpos(100,0)
t2.setpos(-30,0)

t1.speed(5)
t2.speed(5)

def trajectory(tur, dis):
    x = random.choice(range(-dis,dis))
    y = random.choice(range(-dis,dis))
    r = int(abs(x - tur.xcor()) / 1000 * 255)
    b = int(abs(y - tur.ycor()) / 1000 * 255)
    tur.pencolor(255-r,int((r+b)/3),255-b)
    tur.goto(x,y)

for i in range(150):
    t1.pu()
    t2.pu()
    trajectory(t1,300)
    trajectory(t2,300)
    t1.pd()
    t2.pd()
    trajectory(t1,300)
    trajectory(t2,300)