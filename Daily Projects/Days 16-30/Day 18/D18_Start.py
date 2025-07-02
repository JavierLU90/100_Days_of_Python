import turtle as t
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

timmy = t.Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
t.colormode(255)

def random_colours():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# Draw a Square:
def draw_square():
    for _ in range(4):
        timmy.forward(100)
        timmy.left(90)

# Draw a Dotted Line:
def draw_dotted_line():
    for _ in range(50):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

# Draw Different Shapes:
def draw_shapes():
    timmy.penup()
    timmy.setpos(-50, 200)
    timmy.pendown()
    for i in range(3, 11):
        angle = 360 / i
        timmy.pencolor(random.choice(colours))
        for _ in range(i):
            timmy.forward(100)
            timmy.right(angle)

# Draw a Random Walk
def random_walk():
    timmy.pensize(10)
    for _ in range(200):
        timmy.pencolor(random_colours())
        timmy.forward(30)
        timmy.setheading(random.choice(directions))

def draw_spirograph(circles):
    for _ in range(circles):
        timmy.pencolor(random_colours())
        timmy.circle(100)
        timmy.right(360 / circles)

# draw_square()
# draw_dotted_line()
# draw_shapes()
# random_walk()
draw_spirograph(100)

screen = t.Screen()
screen.exitonclick()