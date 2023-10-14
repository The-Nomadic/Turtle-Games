from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    """Snake class handles methods related to the snake(creation, growth, movement)"""
    def __init__(self):
        self.segments = []
        self.crete_snake()
        self.head = self.segments[0]

    def crete_snake(self):
        """Returns the entire snake"""
        for position in positions:
            self.add_box(position)

    def add_box(self, position):
        """Snake starts with 3 boxes(turtles). Returns each box(turtle)"""
        box = Turtle(shape="square")
        box.penup()
        box.color("white")
        box.goto(position)
        self.segments.append(box)

    def extend(self):
        """Increase the snake length by 1 for each food it eats"""
        self.add_box(self.segments[-1].position())

    def move(self):
        """Moves the snake according(forward)"""
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        """Moves the snake according(up)"""
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        """Moves the snake according(down)"""
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        """Moves the snake according(left)"""
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        """Moves the snake according(right)"""
        if self.head.heading() != LEFT:
            self.head.setheading(0)
