# Turtle Artist
# Author: Umar Hassan
# 28 October

import turtle

# A one-of-a-kind drawing

wn = turtle.Screen()
turtle.pensize(3)
turtle.speed(5)
turtle.turtlesize(0.5)
turtle.color("black")
turtle.shape("turtle")

turtle.fillcolor("#E16036")

# round shape of ball
turtle.pu()
turtle.goto(0, -200)
turtle.pd()
turtle.fillcolor("#E16036")
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()

# Right most curved line
turtle.pu()
turtle.goto(148, 135)  # Slightly right of center, bottom of ball
turtle.setheading(180)  # Face upward
turtle.pd()
turtle.circle(135, 180)

turtle.fillcolor("#E16036")

# Middle vertical line
turtle.pu()
turtle.goto(0, -200)
turtle.pd()
turtle.setheading(90)
turtle.forward(400)

turtle.fillcolor("#E16036")

# Left most curved line
turtle.pu()
turtle.goto(-148, -135)  # Slightly left of center, top of ball
turtle.setheading(0)  # Face up
turtle.pd()
turtle.circle(135, 180)

turtle.fillcolor("#E16036")

# middle horizontal line
turtle.pu()
turtle.goto(0, 0)
turtle.pd()
turtle.setheading(0)
turtle.forward(200)
turtle.setheading(180)
turtle.forward(400)

turtle.fillcolor("#E16036")

t = turtle.Turtle()


wn.exitonclick()
