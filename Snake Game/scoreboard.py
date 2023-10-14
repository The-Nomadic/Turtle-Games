from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):
    """ScoreBoard class handles methods related to the score system(calculation, update, message)"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        """Returns the updated scoreboard"""
        self.clear()
        self.write(f"Score = {self.score} | High Score = {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     """Returns the game over message"""
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        """Returns the score"""
        self.score += 1
        self.update_scoreboard()
