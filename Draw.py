import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300, 400)
polygon = turtle.Turtle()

num_si = 6
si_len = 70
angle = 360 / num_si

for i in range (num_si):
    polygon.forward(si_len)
    polygon.right(angle)

turtle.done()