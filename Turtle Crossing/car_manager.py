from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """Deals with all the car functions"""
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        """Returns a car"""
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """Deals with car movement"""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Increases the speed"""
        self.car_speed += MOVE_INCREMENT
