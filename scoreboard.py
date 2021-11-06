from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.n = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-220, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"LEVEL: {self.n}", align="center", font=FONT)

    def increase_the_score(self):
        # increases the score
        self.n += 1
        # clears screen so  that it updates again, and don't get overlap
        self.clear()
        self.update_scoreboard()
