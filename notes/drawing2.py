import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
#AbhijithPrakash
turtle.bgcolor('black')
for x in range(360): #code By ABHIJITHPRAKASH
   t.pencolor(colors[x%6])
   t.width(x/100 + 1)
   t.forward(x)
   t.left(59)
   