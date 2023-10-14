from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Deals with all the player functions"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def move_up(self):
        """Player moves forward by 10"""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Takes the player to the start point"""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Checks if the player has reached the end goal"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
