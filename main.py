import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# screen set-up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

# objects
player = Player()
cars = CarManager()
level = Scoreboard()

screen.listen()
# moving turtles on keystrokes
screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # creates the car.
    cars.create_car()
    # moves the car
    cars.car_move()

    # detecting if player reaches the other side
    if player.ycor() > 290:
        # takes the turtle to the starting point again
        player.start_again()
        # increases speed
        cars.increase_speed()
        # increases level
        level.increase_the_score()

    # detecting the collision of turtle with cars
    for car in cars.all_cars:
        if car.distance(player) < 20:
            player.game_over()
            game_is_on = False

screen.exitonclick()
