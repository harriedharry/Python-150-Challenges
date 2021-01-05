import turtle

scr = turtle.Screen()
scr.bgcolor("yellow")
turtle.pensize(7)
turtle.shape("turtle")

a = ["pink","red","purple"]

for i in range(3):
    turtle.color("black",a[i])
    turtle.begin_fill()
    for i in range(4):
        turtle.left(90)
        turtle.forward(100)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(200)
    turtle.pendown()



turtle.exitonclick()
