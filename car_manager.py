from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []
        self.hideturtle()

    def create_car(self):
        # creates the car, in one out of 6 times the loop runs
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            new_car.penup()
            new_car.goto(x=300, y=new_y)
            self.all_cars.append(new_car)

    def car_move(self):
        # iterable car is now the element in the list
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
