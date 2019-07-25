import turtle
from random import randint

def no_handle(len_line):
    while True:
        if len_line<=10:
            turtle.fd(len_line)
            break
        else:
            turtle.fd(10)
            turtle.rt(11)
            len_line-=10

def handle(len_line,x):
    han = 1
    while True:
        if len_line<=10:
            turtle.fd(len_line)
            break
        else:
            turtle.fd(10)
            if han:
                turtle.rt(x)
                han = 0
            else:
                turtle.lt(x)
                han = 1
            len_line-=10

def draw_black(g_ang,start_x = 0,start_y = 0,start_ang = 0, try_num = 100, hand = False):
    
    ang = start_ang
    x = 1

    while x < try_num + 1:
        turtle.colormode(255) 
        turtle.pencolor(2*x%256,2*x%256,2*x%256)
        
        len_line = x
        turtle.rt(ang + x * g_ang)
        
        if hand:
            handle(len_line,x)
        else:
            no_handle(len_line)

        x = x+1
        turtle.penup()
        turtle.home()
        turtle.goto(start_x,start_y)
        turtle.pendown()

def draw_color(g_ang,start_x = 0,start_y = 0,start_ang = 0, try_num = 100, hand = False):
    
    ang = start_ang
    x = 1

    while x < try_num + 1:
        r = randint(0,255)
        g = randint(0,255) 
        b = randint(0,255)
        
        turtle.colormode(255) 
        turtle.pencolor(r,g,b)
        
        len_line = x
        turtle.rt(ang + x * g_ang)
        
        if hand:
            handle(len_line,x)
        else:
            no_handle(len_line)

        x = x+1
        turtle.penup()
        turtle.home()
        turtle.goto(start_x,start_y)
        turtle.pendown()




turtle.bgcolor('black')
turtle.speed(0)

draw_black(109,start_x = -200,start_y = 200, try_num = 100)
draw_color(109,start_x = -200,start_y = 200, try_num = 100, hand = True)

draw_black(129, try_num = 100)
draw_color(129, try_num = 100)

draw_black(129,start_y = -200, try_num = 100, hand = True)
draw_color(129,start_y = -200, start_ang = 5, try_num = 100, hand = True)

draw_black(59,start_x = 200,start_y = -200, try_num = 100)
draw_color(59,start_x = 200,start_y = -200, try_num = 100)

draw_black(13,start_x = 200,start_y = 200, try_num = 200)

turtle.exitonclick()


