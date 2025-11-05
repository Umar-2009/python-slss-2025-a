# Recursion
# Author: Umar
# 20 October

# We're drawing trees (recursively)

import turtle

mike = turtle.Turtle()


# Dictionary to hold colours
LEAF_COLOURS = {
    "spring": "#dcd6f7",
    "winter": "#a9d2d5",
    "summer": "#f3a712",
    "fall": "#8d5b4c",
}


def draw_tree(level: int, branch_length: float):
    """A recursive function to draw trees.
    level  the levels of branches
    branch_length  length of branch to draw"""
    # : if level is 0, stamp a leaf and return
    if level == 0:
        mike.color(LEAF_COLOURS["spring"])
        mike.stamp()
        mike.color("brown")
        return
    # Recursive case
    mike.forward(branch_length)
    mike.left(50)
    draw_tree(level - 1, branch_length * 0.8)
    mike.right(100)
    draw_tree(level - 1, branch_length * 0.8)
    mike.left(50)
    mike.backward(branch_length)


def factorial(num: int) -> int:
    """Returns the factorial of a given number
    calculated recursively."""
    if num > 1:
        # Multiply the number by the factorial of the previous number
        return num * factorial(num - 1)
    else:
        return 1


factorial(6)
factorial(3)

# Setup turtle
mike.left(90)  # Point turtle upward
mike.color("blue")
mike.pensize(5)
mike.shape("turtle")
mike.penup()
mike.goto(0, -180)
mike.pendown()
# Setup screen
wn = turtle.Screen()
wn.bgcolor("grey")
# Start drawing
draw_tree(5, 100)
# Wait for click to close
wn.exitonclick()
