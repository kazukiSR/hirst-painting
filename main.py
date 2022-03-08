import colorgram as cg
import turtle
import random

colors = cg.extract('image.jpg', 10)
rbgList = []
oneColor = colors[0]
for oneColor in colors:
    rbgList.append(oneColor.rgb)

draw = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
draw.home()
draw.penup()
# print(screen.screensize()) (400, 300)
draw.setpos(-320, -270)
for y in range(10):
    for x in range(10):
        draw.dot(25, random.choice(rbgList))
        if x == 9:
            break
        draw.fd(71)
    if y == 9:
        break
    draw.left(90)
    draw.fd(60)
    draw.right(90)
    draw.setx(-320)


screen.exitonclick()



