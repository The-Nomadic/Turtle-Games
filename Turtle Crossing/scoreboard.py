from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Deals with all the scoreboard functions"""
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Displays the scoreboard"""
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def increase_score(self):
        """Updates the scoreboard"""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Displays game over message"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
