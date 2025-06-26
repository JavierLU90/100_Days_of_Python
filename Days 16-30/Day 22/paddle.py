import turtle as t

MOVE_DISTANCE = 25

class Paddle(t.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.setpos(position)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
