import random
import turtle as t

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_y_pos = [-75, -45, -15, 15, 45, 75]
is_race_on = False

screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")

all_turtles = []
for i in range(6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.setpos(-230, starting_y_pos[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You Won! The {winner} turtle is the winner!")
            else:
                print(f"You Lost... The {winner} turtle won the race.")

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
