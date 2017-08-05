import turtle

colors = ["red", "purple", "blue", "green", "yellow", "orange", "brown"]
sides = 7
t = turtle.Pen()
t.speed(10)
turtle.bgcolor("black")
for x in range(360):
    t.pencolor(colors[x%len(colors)])
    t.width(x*sides/200)
    t.forward(x*3/sides + x)
    t.left(360/sides + 1)

turtle.done()