import turtle as t

ALIGNMENT = "center"
FONT = ("Courier", 22, "bold")

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.setpos(0, 270)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
