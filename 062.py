import turtle

scr = turtle.Screen()
scr.bgcolor("yellow")
turtle.pensize(7)
turtle.shape("turtle")


for i in range(360):
    turtle.forward(1)
    turtle.left(1)


turtle.exitonclick()
