from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-230, 250)
        self.score_update()

    def score_update(self):
        self.write(f"LEVEL {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
