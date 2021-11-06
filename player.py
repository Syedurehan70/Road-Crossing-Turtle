from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 24, "normal")


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.start_again()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def start_again(self):
        # takes the turtle to the starting point again
        self.goto(STARTING_POSITION)

    def game_over(self):
        self.write("GAME OVER", align="center", font=FONT)

