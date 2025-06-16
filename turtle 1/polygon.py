import turtle

win = turtle.Screen()
win.screensize(400,300)
win.bgcolor('black')

t = turtle.Turtle()

t.color('red')
t.width(10)
for i in range(6):
    t.forward(100)
    t.right(360/6)

turtle.done()