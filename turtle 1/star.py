import turtle

win = turtle.Screen()
win.screensize(400,300)
win.bgcolor('black')

t = turtle.Turtle()

t.color('red')
t.width(10)
for i in range(3):
    t.forward(100)
    t.left(360/3)

t.left(90)
t.penup()
t.forward(65)
t.pendown()
t.right(90)
for i in range(3):
    t.forward(100)
    t.right(360/3)

turtle.done()