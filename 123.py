import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen", "yellow")
t.shapesize(1)


for x in range(4):
    t.forward(200)
    t.left(90)

time.sleep(10)