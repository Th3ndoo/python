import turtle

win = turtle.Screen()
win.screensize(400,300)
win.bgcolor('black')
t = turtle.Turtle()
t.color('red')
t.width(3)
side = 10
while True:
    t.forward(side)
    t.right(90)
    side +=5